from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import CV
from .models import Employment
from .models import Education

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def cv(request):
    cv = CV.objects.all()[:1].get()
    return render(request, 'blog/cv.html', {'cv': cv})

def home_page(request):
    return render(request, 'blog/home_page.html')

