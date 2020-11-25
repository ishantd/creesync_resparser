from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt


class ResumeParser(APIView):
    parser_class = (FileUploadParser,)

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")
        f = request.data['file']
        if not ('.pdf' in f.name):
            raise ParseError("File format not supported")
        return Response(status=200)
