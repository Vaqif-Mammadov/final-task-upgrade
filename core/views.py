from django.shortcuts import render,redirect,get_object_or_404


# Create your views here.
def home_view(request):
    return render (request, "index.html")

def home2_view(request):
    return render (request, "index-2.html")

def about_view(request):
    return render (request, "about.html")

def services_view(request):
    return render (request, "services.html")

def pricing_view(request):
    return render (request, "pricing.html")

def contact_view(request):
    return render (request, "contact.html")

def blog_masonry_view(request):
    return render (request, "blog-masonry.html")

def blog_view(request):
    return render (request, "blog.html")

def single_post_1_view(request):
    return render (request, "single-post-1.html")

def single_post_2_view(request):
    return render (request, "single-post-2.html")

def not_found_404_view(request):
    return render (request, "404.html")