from django.db import models

# Create your models here.
class Resume(models.Model):
    resume_field = models.FileField(upload_to='resumes/', null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    college_name = models.TextField(null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    total_experience = models.FloatField(null=True, blank=True)