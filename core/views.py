from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.cache import cache
from .models import Profile
from django.http import JsonResponse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import random
import string
import logging


# Create your views here.

def generate_verification_code():
    return ''.join(random.choices(string.digits, k=6))


def send_verification_email(email, code):
    subject = 'Your Verification Code'
    message = f'Your verification code is {code}.'
    from_email = 'dervisvaqif@gmail.com'
    try:
        mail_sent = send_mail(subject, message, from_email, [email])
        return mail_sent > 0
    except Exception as e:
        print(f'Error sending email: {e}')
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
                    return JsonResponse({'message': 'A verification code has been sent to your email.'})
                else:
                    return JsonResponse({'message': 'Failed to send verification code. Please try again.'}, status=500)
            else:
                return JsonResponse({'message': 'Please enter a valid email address.'}, status=400)
        else:
            return JsonResponse({'message': 'Invalid form submission.'}, status=400)
    return JsonResponse({'message': 'Invalid request method.'}, status=405)


def get_verification_code(request):
    response = JsonResponse({'verification_code': request.session.get('verification_code')})
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
    
def user_data(request):
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


logger = logging.getLogger(__name__)

def user_auth(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'index.html', {'form': form})
    else:
        form = AuthenticationForm()

def home_view(request):
    user_auth(request)
    return render(request, 'index.html')

def home2_view(request):
    user_auth(request)
    return render (request, "index-2.html")

def about_view(request):
    user_auth(request)
    return render (request, "about.html")

def services_view(request):
    user_auth(request)
    return render (request, "services.html")

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