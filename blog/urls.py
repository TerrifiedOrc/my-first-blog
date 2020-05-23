from django.urls import path
from . import views
from .models import Employment

urlpatterns = [
path('', views.home_page, name='home_page'),
path('post_list', views.post_list, name='post_list'),
path('cv', views.cv, name='cv'),
path('cv/update_personal_details', views.update_personal_details, name='update_personal_details'),
path('cv/employment/<int:id>/delete', views.employment_delete, name='employment_delete'),
path('cv/employment/add', views.employment_add, name='employment_add'),
path('cv/education/<int:id>/delete', views.education_delete, name='education_delete'),
path('cv/education/add', views.education_add, name='education_add'),
]