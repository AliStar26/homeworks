import requests
from django.shortcuts import render

def index(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()
    context ={
        'posts': posts
    }
    return render(request, 'index.html', context)
