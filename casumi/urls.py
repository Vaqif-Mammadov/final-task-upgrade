"""
URL configuration for casumi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# from article.views import home__view, about__view, contact__view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view,name="index"),
    path('home2/', home2_view,name="home2"),
    path('about/', about_view,name="about"),
    path('services/', services_view,name="services"),
    path('pricing/', pricing_view,name="pricing"),
    path('contact/', contact_view,name="contact"),
    path('blog_masonry/', blog_masonry_view,name="blog-m"),
    path('blog/', blog_view,name="blog"),
    path('blogjs/',blog_view_for_js,name="blogjs"),
    path('single_posts/<int:id>/', single_posts_view,name="single_posts"),
    # path('single_post_1/', single_post_1_view,name="single-p1"),
    # path('single_post_2/', single_post_2_view,name="single-p2"),
    path('not_found_404/', not_found_404_view,name="404"),
    path('api/users/', user_data, name='user_data'),
    path('email_verification/', email_verification_view, name='email_verification'),
    path('get-verification-code/', get_verification_code, name='get_verification_code'),
    path('login/', login_view, name='login_view'),
    path('signup/',signup_view, name='signup'),
    path('password-change/', password_change, name='password_change'),
    path('update-profile-picture/', update_profile_picture, name='update_profile_picture'),
    path('addcomment/', addcomment, name='addcomment'),
    path('add_reply/<int:comment_id>/', add_reply, name='add_reply'),
    path('usercontact/', usercontact_view, name='usercontact'),
    path('faq/',faq_view,name="faq"),
    path('send-newsletter/', send_newsletter_message, name='send_newsletter'),


    # path('detail/<int:id', detail_view,name="detail"),
    
    # path("account/", include("account.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
