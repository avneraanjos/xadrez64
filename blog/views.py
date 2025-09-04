from django.http import HttpResponse
from django.shortcuts import render # Used for rendering templates
from django.template import loader
from .models import Post, Category, Comment


def home_view(request):
    """
    A simple view that returns a plain text response.
    """
    html_template = loader.get_template('home/index.html')
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return HttpResponse(html_template.render(request=request))


