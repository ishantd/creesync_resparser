from django.urls import include, path
from . import views

urlpatterns = [
  path('resume_upload', views.resume, name='resume_upload')
]
