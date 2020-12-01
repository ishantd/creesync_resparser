from django.shortcuts import render

# Create your views here.
def resume(request):

    return render(request, 'home/resume.html')