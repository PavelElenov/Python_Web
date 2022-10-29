from django import http
from django.shortcuts import render


def show(request):
    return http.HttpResponse('It works!')
