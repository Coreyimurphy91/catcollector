from django.shortcuts import render
from django.http import HttpResponse

# temporary add cats class
class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

    def __str__(self):
        return f"{self.name}"
    
cats = [
    Cat('Rufus', 'Tabby', 'crazy', 103),
    Cat('Simba', 'Lion', 'brave', 5),
    Cat('Garfield', 'Orange-Tabby', 'likes lasagna', 9),
]

# Create your views here.
def index(request):
    return render(request, 'index.html', { 'cats': cats})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def cats_index(request):
    return render(request, 'cats/index.html', { 'cats': cats})