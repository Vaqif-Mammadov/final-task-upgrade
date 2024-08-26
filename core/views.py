from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponseForbidden,HttpResponse
from django.core.cache import cache
from .models import Profile,Service
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import random
import string
import json
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth.forms import SetPasswordForm
from django.conf import settings
from .forms import ProfilePictureForm


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'home.html', {'form': form})

def generate_verification_code():
    return ''.join(random.choices(string.digits, k=6))


def send_verification_email(email, code):
    subject = 'Your Verification Code'
    message = f'Your verification code is {code}.'
    from_email = 'casuminew@outlook.com'
    try:
        mail_sent = send_mail(subject, message, from_email, [email])
        return mail_sent > 0
    except Exception as e:
        return False

@csrf_exempt
def email_verification_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        form_id = request.POST.get('form_id')
        if form_id and email:
            if email:
                code = generate_verification_code()
                request.session['verification_code'] = code
                if send_verification_email(email, code):
                    return JsonResponse({'status': 'success','message': 'A verification code has been sent to your email.'})
                else:
                    return JsonResponse({'status': 'error','message': 'Failed to send verification code. Please try again.'}, status=500)
            else:
                return JsonResponse({'status': 'error','message': 'Please enter a valid email address.'}, status=400)
        else:
            return JsonResponse({'status': 'error','message': 'Invalid form submission.'}, status=400)
    return JsonResponse({'status': 'error','message': 'Invalid request method.'}, status=405)


@csrf_exempt
def get_verification_code(request):
    if request.method == 'GET':
        token = request.headers.get('Authorization')
        if token == 'bvmVNBMBMHB24512vbnmmm45vbgfhvn53VGBHJbjghj275fgcgvnf':
            verification_code = request.session.get('verification_code')
            response = JsonResponse({'verification_code': verification_code})
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
            return response
        else:
            return JsonResponse({'status': 'error','message': 'Unauthorized access.'}, status=403)
    return JsonResponse({'status': 'error','message': 'Invalid request method.'}, status=405)

def user_data(request):
    token = request.headers.get('Authorization', '').split(' ')[-1]
    if token != 'bvmVNBMBMHB24512vbnmmm45vbgfhvn53VGBHJbjghj275fgcgvnf':
        return HttpResponseForbidden('Unauthorized')
    users = Profile.objects.all()
    user_data = []
    for user in users:
        user_data.append({
            'id': user.id,
            'email': user.email,
            'phone': user.phone_number,
            'username': user.username,
        })
    return JsonResponse(user_data, safe=False)

username_global = None
password_global = None

@csrf_exempt
def login_view(request):
    global username_global
    global password_global
    if request.method == 'POST':
        username_global = request.POST.get('username')
        password_global = request.POST.get('password')
        print(username_global)
    return render(request,'index.html')

def user_auth(request):
    if request.method == 'POST':
        form_id = request.POST.get('form_id')
        action = request.POST.get('action')
        if form_id == 'securitypasswordform':
            user = authenticate(username=username_global, password=password_global)
            if user is not None:
                login(request, user)
        elif action == 'logout':
            logout(request)
    else:
        form = AuthenticationForm()

@csrf_exempt
def password_change(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_password1 = data.get('new_password1')
            new_password2 = data.get('new_password2')
            email = data.get('email')
            if new_password1 and new_password2 and new_password1 == new_password2:
                user = User.objects.filter(email=email).first()
                if user:
                    form = SetPasswordForm(user, {'new_password1': new_password1, 'new_password2': new_password2})
                    if form.is_valid():
                        form.save()
                        return JsonResponse({'status': 'success', 'message': 'Password reset successful.'})
                    else:
                        return JsonResponse({'status': 'error', 'message': 'Invalid password.'}, status=400)
                return JsonResponse({'status': 'error', 'message': 'User not found.'}, status=400)
            return JsonResponse({'status': 'error', 'message': 'Passwords do not match.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON.'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


#
@login_required
def update_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            new_picture_url = request.user.profile.profile_picture.url
            return JsonResponse({'success': True, 'new_picture_url': new_picture_url})
        else:
            return JsonResponse({'success': False, 'error': 'Form is not valid'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


def home_view(request):
    user_auth(request)
    services=Service.objects.all()
    context={'services':services
             }
    return render(request, 'index.html',context)

def home2_view(request):
    user_auth(request)
    return render (request, "index-2.html")

def about_view(request):
    user_auth(request)
    return render (request, "about.html")

@login_required
def services_view(request):
    user_auth(request)
    services=Service.objects.all()
    context={'services':services
             }
    return render (request, "services.html",context)

def pricing_view(request):
    user_auth(request)
    return render (request, "pricing.html")


def contact_view(request):
    user_auth(request)
    return render (request, "contact.html")

def blog_masonry_view(request):
    user_auth(request)
    return render (request, "blog-masonry.html")

def blog_view(request):
    user_auth(request)
    return render (request, "blog.html")

def single_post_1_view(request):
    user_auth(request)
    return render (request, "single-post-1.html")

def single_post_2_view(request):
    user_auth(request)
    return render (request, "single-post-2.html")

def not_found_404_view(request):
    user_auth(request)
    return render (request, "404.html")




# def detail_view(request,id):
#     return HttpResponse ("Detail:",+ str (id))