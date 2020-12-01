from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from pyresparser import ResumeParser
from resume_api.models import *


def parse_resume_full(resume):
    path = f'/home/ishant/ishant_linux/farzi/resumeparser/media/{resume.resume_field.name}'
    print(path)
    data = ResumeParser(path).get_extracted_data()
    return data

class ResumeParserAPI(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, format=None):
        print(request.data)
        if 'upload' not in request.data:
            raise ParseError("Empty content")
        f = request.data['upload']
        new_resume = Resume(resume_field=f)
        new_resume.save()
        data = parse_resume_full(new_resume)
        # update_status = update_resume_data(data, resume)
        return JsonResponse(data, status=200)

