from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World..! 8)')

def about(request):
    return HttpResponse('About page')

def contact(request):
    return HttpResponse('Contact me please I am lonely')

def blog(request):
    return HttpResponse('Blogs remind me of MySpace')