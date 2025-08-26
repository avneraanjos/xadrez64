from django.http import HttpResponse
from django.shortcuts import render # Used for rendering templates

def home_view(request):
    """
    A simple view that returns a plain text response.
    """
    return HttpResponse("Welcome to my Django application!")