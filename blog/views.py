from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .models import CV
from .models import Employment
from .models import Education
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def employment(request, id):
    obj = get_object_or_404(Employment, id=id)
    return render(request, 'blog/employment.html', {'employment': employment})

def cv(request):
    cv = CV.objects.all()[:1].get()
    employments = []

    for employment in Employment.objects.all():
        if (employment.foreignKey == cv):
            employments.append(employment)

    return render(request, 'blog/cv.html', {'cv': cv, 'employments': employments})

def home_page(request):
    return render(request, 'blog/home_page.html')

def employment_delete(request, id):
    obj = get_object_or_404(Employment, id=id)
    if request.method == "POST":
        obj.delete()
    return redirect('cv')

def employment_add(request):
    id = request.POST["id"]
    if id != '0':
        employment = get_object_or_404(Employment, id=id)
        employment.title = request.POST["title"]
        employment.address = request.POST["address"]
        employment.desc = request.POST["desc"]
        employment.skills = request.POST["skills"]
        employment.startDate = request.POST["startDate"]
        employment.endDate = request.POST["endDate"]
        employment.foreignKey = CV.objects.all()[:1].get()
        employment.save()
    else:
        title = request.POST["title"]
        address = request.POST["address"]
        desc = request.POST["desc"]
        skills = request.POST["skills"]
        startDate = request.POST["startDate"]
        endDate = request.POST["endDate"]
        foreignKey = CV.objects.all()[:1].get()

        employment = Employment(title=title, address=address, 
        desc=desc, skills=skills, startDate=startDate,
        endDate=endDate,foreignKey=foreignKey)
        employment.save()
    return redirect('cv')
