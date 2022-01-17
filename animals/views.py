from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, Http404
from .models import *
from .forms import AnnouncementForm
from django.conf import settings
from django.views.generic import View


menu = [{'title': 'О проекте', 'url_name': 'about'},
        {'title': 'Опубликовать объявление', 'url_name': 'add_note'},
        {'title': 'Войти', 'url_name': 'login'},
        {'title': 'Регистрация', 'url_name': 'signup'},
        {'title':'Выйти', 'url_name': 'logout'},
        ]

class AddNote(View):
    def get(self,request):
        form = AnnouncementForm()
        return render(request, 'animals/addpost.html', context={'form': form, 'menu': menu})

    def post(self, request):
        pos_form = AnnouncementForm()
        user = request.user
        if request.method == 'POST':
            pos_form = AnnouncementForm(request.POST, request.FILES)
            if pos_form.is_valid():
                pos_form.save()
                return redirect('all_animals')
        data = {'pos_form': pos_form, 'media_url': settings.MEDIA_URL}
        return render(request, 'animals/all_animals.html', data)


def all_animals(request):
    announcement = Announcement.objects.all().order_by('-data')
    context = {
        'announcement': announcement,
        'title': 'Пропавшие животные',
        'menu': menu
    }
    return render(request, 'animals/all_animals.html', context=context)

def show_cat(request):
    announcement = Announcement.objects.filter(animal__breed__animal_type__clases='CAT')
    if announcement.exists():
        context = {
            'announcement': announcement,
            'title': 'Пропавшие животные',
            'menu': menu
        }
        return render(request, 'animals/category.html', context=context)
    else:
        return render(request, 'animals/nonannouncement.html')


def show_dog(request):
    announcement = Announcement.objects.filter(animal__breed__animal_type__clases='DOG')
    if announcement.exists():
        context = {
            'announcement': announcement,
            'title': 'Пропавшие животные',
            'menu': menu
        }
        return render(request, 'animals/category.html', context=context)
    else:
        return render(request, 'animals/nonannouncement.html')

def show_bird(request):
     announcement = Announcement.objects.filter(animal__breed__animal_type__clases='BIRD')
     if announcement.exists():
        context = {
            'announcement': announcement,
            'title': 'Пропавшие животные',
            'menu': menu
        }
        return render(request, 'animals/category.html', context=context)
     else:
         return render(request, 'animals/nonannouncement.html')


def show_other(request):
    announcement = Announcement.objects.filter(animal__breed__animal_type__clases='OTHER')
    if announcement.exists():
        context = {
            'announcement': announcement,
            'title': 'Пропавшие животные',
            'menu': menu
        }
        return render(request, 'animals/category.html', context=context)
    else:
        return render(request, 'animals/nonannouncement.html')


def about(request):
    return render(request, 'animals/about.html', {'menu': menu, 'title': 'Главная страница'})
def home(request):
    return render(request, 'animals/about.html', {'menu': menu, 'title': 'Главная страница'})
def partner(request):
    return render(request, 'animals/partner.html', {'menu': menu, 'title': 'Главная страница'})
def help(request):
    return render(request, 'animals/help.html', {'menu': menu, 'title': 'Главная страница'})
