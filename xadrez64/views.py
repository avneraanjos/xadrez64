from django.http import HttpResponse
from django.shortcuts import render # Used for rendering templates
from django.template import loader
from django import template


def home_view(request):
    """
    A simple view that returns a plain text response.
    """
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(request=request))
