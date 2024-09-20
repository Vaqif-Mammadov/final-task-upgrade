from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponseForbidden, HttpResponse
from django.core.cache import cache
from .models import *
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import random
import string
import json
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth.forms import SetPasswordForm
from django.conf import settings
from .forms import ProfilePictureForm, ReplyForm, User_contactForm, FAQForm
import re
from django.core import serializers
from django.core.paginator import Paginator



def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            login(request, user)
            return redirect("index")
    else:
        form = SignupForm()
    return render(request, "index.html", {"form": form})


def generate_verification_code():
    return "".join(random.choices(string.digits, k=6))


def send_verification_email(email, code):
    subject = "Your Verification Code"
    message = f"Your verification code is {code}."
    from_email = "casumic2024@outlook.com"
    try:
        mail_sent = send_mail(subject, message, from_email, [email])
        return mail_sent > 0
    except Exception as e:
        return False


@csrf_exempt
def email_verification_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        form_id = request.POST.get("form_id")
        if form_id and email:
            if email:
                code = generate_verification_code()
                request.session["verification_code"] = code
                print(email, code)
                if send_verification_email(email, code):
                    return JsonResponse(
                        {
                            "status": "success",
                            "message": "A verification code has been sent to your email.",
                        }
                    )
                else:
                    return JsonResponse(
                        {
                            "status": "error",
                            "message": "Failed to send verification code. Please try again.",
                        },
                        status=500,
                    )
            else:
                return JsonResponse(
                    {
                        "status": "error",
                        "message": "Please enter a valid email address.",
                    },
                    status=400,
                )
        else:
            return JsonResponse(
                {"status": "error", "message": "Invalid form submission."}, status=400
            )
    return JsonResponse(
        {"status": "error", "message": "Invalid request method."}, status=405
    )


@csrf_exempt
def get_verification_code(request):
    if request.method == "GET":
        token = request.headers.get("Authorization")
        if token == "bvmVNBMBMHB24512vbnmmm45vbgfhvn53VGBHJbjghj275fgcgvnf":
            verification_code = request.session.get("verification_code")
            response = JsonResponse({"verification_code": verification_code})
            response["Cache-Control"] = (
                "no-store, no-cache, must-revalidate, proxy-revalidate"
            )
            response["Pragma"] = "no-cache"
            response["Expires"] = "0"
            return response
        else:
            return JsonResponse(
                {"status": "error", "message": "Unauthorized access."}, status=403
            )
    return JsonResponse(
        {"status": "error", "message": "Invalid request method."}, status=405
    )


def user_data(request):
    token = request.headers.get("Authorization", "").split(" ")[-1]
    if token != "bvmVNBMBMHB24512vbnmmm45vbgfhvn53VGBHJbjghj275fgcgvnf":
        return HttpResponseForbidden("Unauthorized")
    users = Profile.objects.all()
    user_data = []
    for user in users:
        user_data.append(
            {
                "id": user.id,
                "email": user.email,
                "phone": user.phone_number,
                "username": user.username,
            }
        )
    return JsonResponse(user_data, safe=False)


username_global = None
password_global = None


@csrf_exempt
def login_view(request):
    global username_global
    global password_global
    if request.method == "POST":
        username_global = request.POST.get("username")
        password_global = request.POST.get("password")
        print(username_global, password_global)
    return render(request, request.path)


def user_auth(request):
    if request.method == "POST":
        form_id = request.POST.get("form_id")
        action = request.POST.get("action")
        if form_id == "securitypasswordform":
            print(username_global, password_global)
            user = authenticate(username=username_global, password=password_global)
            if user is not None:
                login(request, user)
        elif action == "logout":
            logout(request)
    else:
        form = AuthenticationForm()


@csrf_exempt
def password_change(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            new_password1 = data.get("new_password1")
            new_password2 = data.get("new_password2")
            email = data.get("email")
            print(email)
            if new_password1 and new_password2 and new_password1 == new_password2:
                user = User.objects.filter(email=email).first()
                if user:
                    form = SetPasswordForm(
                        user,
                        {
                            "new_password1": new_password1,
                            "new_password2": new_password2,
                        },
                    )
                    if form.is_valid():
                        form.save()
                        return JsonResponse(
                            {
                                "status": "success",
                                "message": "Password reset successful.",
                            }
                        )
                    else:
                        return JsonResponse(
                            {"status": "error", "message": "Invalid password."},
                            status=400,
                        )
                return JsonResponse(
                    {"status": "error", "message": "User not found."}, status=400
                )
            return JsonResponse(
                {"status": "error", "message": "Passwords do not match."}, status=400
            )
        except json.JSONDecodeError:
            return JsonResponse(
                {"status": "error", "message": "Invalid JSON."}, status=400
            )
    return JsonResponse(
        {"status": "error", "message": "Invalid request method"}, status=405
    )


@login_required
def update_profile_picture(request):
    if request.method == "POST":
        form = ProfilePictureForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            new_picture_url = request.user.profile.profile_picture.url
            return JsonResponse({"success": True, "new_picture_url": new_picture_url})
        else:
            return JsonResponse({"success": False, "error": "Form is not valid"})
    return JsonResponse({"success": False, "error": "Invalid request"})


# homeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee


def home_view(request):
    user_auth(request)
    services = Service.objects.all()
    servs = Serv.objects.all()
    praises = Praise.objects.all()
    news = New.objects.all()
    socials = Social.objects.all()
    socials_three = Social.objects.filter(active=True)[:3]
    socials_six = Social.objects.filter(active=True)[:6]
        
    context = {
        "services": services,
        "servs": servs,
        "praises": praises,
        "news": news,
        "socials": socials,
        "socials_three": socials_three,
        "socials_seven": socials_six,
        'news_length': len(news)
    }
    return render(request, "index.html", context)


# homeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee


# HOME222222222222222222222222222222222222222222222222222222222222222
def home2_view(request):
    user_auth(request)
    slickboxes = Slickbox.objects.all()
    consultants = Consultant.objects.all()
    plans = Plan.objects.all()
    socials = Social.objects.all()

    for plan in plans:
        try:
            plan_features = plan.get_my_list()
            print(f"Plan: {plan.name}, Features: {plan_features}")
        except Exception as e:
            print(f"Error with plan {plan.name}: {e}")

    context = {
        "consultants": consultants,
        "slickboxes": slickboxes,
        "plans": plans,
        "socials": socials,
    }

    return render(request, "index-2.html", context)


# HOME222222222222222222222222222222222222222222222222222222222222222


def about_view(request):
    user_auth(request)
    consultants = Consultant.objects.all()
    socials = Social.objects.all()
    context = {
        "consultants": consultants,
        "socials": socials,
    }
    return render(request, "about.html", context)


# SERVICEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
def services_view(request):
    user_auth(request)
    services = Service.objects.all()
    sponsors = Sponsor.objects.all()
    socials = Social.objects.all()
    context = {
        "services": services,
        "sponsors": sponsors,
        "socials": socials,
    }
    return render(request, "services.html", context)


# SERVICEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE


# PRICINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
def pricing_view(request):
    user_auth(request)
    socials = Social.objects.all()
    plans = Plan.objects.all()
    for plan in plans:
        try:
            plan_features = plan.get_my_list()
            print(f"Plan: {plan.name}, Features: {plan_features}")
        except Exception as e:
            print(f"Error with plan {plan.name}: {e}")

    context = {
        "plans": plans,
        "socials": socials,
    }
    return render(request, "pricing.html", context)


# PRICINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG


# CONTACTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

def contact_view(request):
    user_auth(request)
    contacts = Contact.objects.all()
    socials = Social.objects.all()
    context = {
        "contacts": contacts,
        "socials": socials,
    }
    return render(request, "contact.html", context)


# CONTACTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT


# BLOGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
def blog_view(request):
    user_auth(request)
    news = New.objects.all()
    socials = Social.objects.all()
    context = {
        "news": news,
        "socials": socials,
        'news_length':len(news)
    }
    return render(request, "blog.html", context)



def blog_view_for_js(request):
    news = New.objects.all()
    news_list = list(news.values('id','image','image_icon', 'category', 'category2','title','content','name_lastname','icon','history','topimg','midimg','botimg'))  
    return JsonResponse({"news": news_list})  


def send_newsletter_message(request):
    if request.method == "POST":
        message_text = request.POST.get("message")
        if message_text:
            try:
                user = request.user
                profile = Profile.objects.get(user=user)
                mail1 = profile.email

                message_instance = NewsletterMessage(
                    user=user,
                    mail1=mail1,
                    subject="Newsletter Message",
                    message=message_text,
                )
                message_instance.save()

                to_email = Contact.objects.first().mail1
                from_email = mail1
                subject = "Newsletter Message"
                message = f"From: {from_email}\n\n{message_text}"

                send_mail(subject, message, from_email, [to_email])

                response_data = {
                    "success": True,
                    "message": "Your message has been sent successfully!",
                }
            except Profile.DoesNotExist:
                response_data = {
                    "success": False,
                    "message": "Profile not found for this user.",
                }
            except Contact.DoesNotExist:
                response_data = {
                    "success": False,
                    "message": "Contact email not found.",
                }
            except Exception as e:
                response_data = {"success": False, "message": str(e)}
        else:
            response_data = {"success": False, "message": "No message text provided."}

        return JsonResponse(response_data)

    return JsonResponse(
        {"success": False, "message": "Invalid request method."}, status=400
    )


# BLOGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG


# BLOG MASONRYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
def blog_masonry_view(request):
    user_auth(request)
    news = New.objects.all()
    news_list = New.objects.all()
    paginator = Paginator(news_list, 6) 
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
    socials=Social.objects.all()
    context = {
        "news": news,
        "page_obj": page_obj,
        "socials":socials,
    }
    return render(request, "blog-masonry.html", context)


# BLOG MASONRYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY


# BLOG_POST111111111111111111111111111111111111111111111111111111111111
# def single_post_1_view(request):
#     user_auth(request)
#     comments = Comment.objects.all()
#     count = len(comments)
#     profile_name = request.user.profile.username
#     news = New.objects.all()
#     profile_image = request.user.profile.profile_picture
#     consultants = Consultant.objects.all()
#     socials=Social.objects.all()
#     context = {
#         "news": news,
#         "comments": comments,
#         "profile_name": profile_name,
#         "profile_image": profile_image,
#         "count": count,
#         "consultants": consultants,
#         "socials":socials,
#     }
#     return render(request, "single-post-1.html", context)


# BLOG_POST111111111111111111111111111111111111111111111111111111111111


# BLOG_POST22222222222222222222222222222222222222222222222222222222222222222222222222222
# def single_post_2_view(request):
#     user_auth(request)
#     comments = Comment.objects.all()
#     count = len(comments)
#     profile_name = request.user.profile.username
#     news = New.objects.all()
#     profile_image = request.user.profile.profile_picture
#     socials=Social.objects.all()
#     context = {
#         "news": news,
#         "comments": comments,
#         "profile_name": profile_name,
#         "profile_image": profile_image,
#         "count": count,
#         "socials":socials,
#     }

#     return render(request, "single-post-2.html", context)


# BLOG_POST22222222222222222222222222222222222222222222222222222222222222222222222222222


# POSTSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS


def single_posts_view(request, id):
    user_auth(request)
    comments = Comment.objects.all()
    count = len(comments)
    # profile_name = request.user.profile.username
    new = get_object_or_404(New, id=id)
    news = New.objects.all()
    part1 = new.content[:920]
    part2 = new.content[920:1900]
    part3 = new.content[1900:]
    # profile_image = request.user.profile.profile_picture
    consultants = Consultant.objects.all()
    socials=Social.objects.all()
    context = {
        "new": new,
        "news": news,
        "comments": comments,
        # "profile_name": profile_name,
        # "profile_image": profile_image,
        "count": count,
        "consultants": consultants,
        "part1": part1,
        "part2": part2,
        "part3": part3,
        "socials":socials,
    }

    return render(request, "single_posts.html", context)


# POSTSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS


def not_found_404_view(request):
    user_auth(request)
    socials=Social.objects.all()
    context = {
        "socials":socials,
    }

    return render(request, "404.html",context)


def addcomment(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            comment = Comment(
                profile_id=request.user.profile,
                email=data.get("email"),
                url=data.get("url"),
                comment=data.get("comment"),
            )
            comment.save()
            return JsonResponse(
                {"status": "success", "message": "Comment added successfully"}
            )
        except json.JSONDecodeError:
            return JsonResponse(
                {"status": "error", "message": "Invalid JSON"}, status=400
            )
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


def add_reply(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        data = json.loads(request.body)
        form = ReplyForm(data)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = comment
            reply.user = request.user  # Daxil olmuş istifadəçini təyin edirik
            reply.save()
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "error", "message": form.errors})
    return JsonResponse({"status": "error", "message": "Invalid request"})


user = User.objects.first()


def usercontact_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = User_contactForm(data)
        if form.is_valid():
            usercontact = form.save(commit=False)
            usercontact.user = request.user
            usercontact.save()
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "error", "message": form.errors})
    return JsonResponse({"status": "error", "message": "Invalid request"})


@csrf_exempt
def faq_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            full_name = data.get("full_name")
            email = data.get("email")
            phone = data.get("phone")
            message = data.get("message")
            message = message.lower().strip()
            normalized_message = re.sub(r"\W+", " ", message)
            faq, created = FAQQuestion.objects.get_or_create(
                phone=phone,
                email=email,
                normalized_message=normalized_message,
                defaults={"full_name": full_name},
            )
            if not created:
                faq.count += 1
                faq.save()

            return JsonResponse(
                {
                    "status": "success",
                    "message": "Your question has been submitted successfully.",
                }
            )
        except (ValueError, TypeError, KeyError) as e:
            return JsonResponse(
                {"status": "error", "message": "Invalid data."}, status=400
            )
    user_auth(request)
    faqs = FAQQuestion.objects.prefetch_related("answers").all()
    seen_messages = set()
    unique_faqs = []

    for faq in faqs:
        if faq.message not in seen_messages:
            seen_messages.add(faq.message)
            unique_faqs.append(faq)

    return render(request, "FAQ.html", {"faqs": unique_faqs})


