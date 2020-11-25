from django.db import models

# Create your models here.
class Resume(models.Model):
    resume_field = models.FileField(upload_to='resumes/', null=True)

class ResumeDetail(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    college = models.TextField(null=True, blank=True)