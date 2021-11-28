from django.shortcuts import render,redirect, HttpResponse
from .models import *
from .forms import AddPostNote

menu = [{'title':'о проекте','url_name':'about'},
        {'title':'опубликовать новость', 'url_name': 'add_note'},
         {'title':'войти', 'url_name': 'login'},
          {'title':'регистрация', 'url_name':'reristration'}
        ]

category = (
    ('кошки','КОШКИ'),
    ('собаки', 'СОБАКИ'),
    ('птицы','ПТИЦЫ'),
    ('земноводные','ЗЕМНОВОДНЫЕ'),
    ('иное','ИНОЕ'),
)

def home(request):
    posts = Note.objects.all()
    context = {
        'menu':menu,
        'posts':posts,
        'title': 'Главная страница'
    }
    return render(request, 'animals/home.html', context=context)

def about(request):
    return render(request, 'animals/about.html', {'menu':menu, 'title': 'Главная страница'})

def add_note(request):
    form = AddPostNote()
    return render(request, 'animals/addpost.html',{'form':form, 'menu':menu, 'title':'Главная страница'})

def login(request):
    return HttpResponse ('Вход')
def reristration(request):
    return HttpResponse ('Регистрация')

def show_post(request, post_id):
    return HttpResponse (f'заметка id {post_id}')