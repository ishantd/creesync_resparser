from django.urls import include, path
from resume_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('resume', views.ResumeParser.as_view(), name='resume')
]

urlpatterns = format_suffix_patterns(urlpatterns)