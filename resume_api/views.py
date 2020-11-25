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
    path = f'/home/ishant/ishant_linux/farzi/resumeparser{resume.resume_field.url}'
    data = ResumeParser(path).get_extracted_data()
    return data
class ResumeParserAPI(APIView):
    parser_class = (FileUploadParser,)

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")
        f = request.data['file']
        if not ('.pdf' in f.name):
            raise ParseError("File format not supported")

        new_resume = Resume(resume_field=f)
        new_resume.save()
        data = parse_resume_full(new_resume)     
        return JsonResponse(data, status=200)

