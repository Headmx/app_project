from django.shortcuts import render,redirect, HttpResponse, get_object_or_404, Http404
from .models import *
from .forms import AddType, AddAnimal,AddAnnouncement,AddDetail, AddLocation
from django.conf import settings

menu = [{'title':'о проекте','url_name':'about'},
        {'title':'опубликовать новость', 'url_name': 'add_note'},
         {'title':'войти', 'url_name': 'login'},
          {'title':'регистрация', 'url_name':'reristration'}
        ]

def add_note(request):
    imgs = Animal.objects.all()
    error = ''
    if request.method == 'POST':
        type_form = AddType(request.POST or None)
        ditail_form = AddDetail(request.POST or None)
        animal_form = AddAnimal(request.POST, request.FILES)
        location_form = AddLocation(request.POST or None)
        announcement_form = AddAnnouncement(request.POST or None)

        if type_form.is_valid() and ditail_form.is_valid() and animal_form.is_valid() and location_form.is_valid() and announcement_form.is_valid():
            add_note = type_form.save(commit=False)
            add_detail = ditail_form.save(commit=False)
            add_animal = animal_form.save(commit=False)
            add_location = location_form.save(commit=False)
            add_announcement= announcement_form.save(commit=False)
            add_note.save()
            add_detail.save()
            add_animal.save()
            add_location.save()
            add_announcement.save()
            return redirect('all_animals')
        else:
            error = 'error form'

    type = AddType()
    detail = AddDetail()
    animal = AddAnimal()
    location = AddLocation()
    announcement = AddAnnouncement()
    data ={'type':type,'ditail':detail,'animal':animal,'location':location,'announcement':announcement,'error':error,'imgs':imgs,'menu':menu, 'title':'Добавить заметку','media_url':settings.MEDIA_URL}
    return render(request, 'animals/addpost.html', data)

def all_animals(request):
    type = Type.objects.all()
    detail = Details_type.objects.all()
    animal = Animal.objects.all()
    location = Location.objects.all()
    announcement = Announcement.objects.all()
    context = {
        'menu':menu,
        'type':type,
        'detail':detail,
        'animal':animal,
        'location':location,
        'announcement':announcement,
        'title': 'Пропавшие животные'
    }
    return render(request, 'animals/all_animals.html', context=context)


def about(request):
    return render(request, 'animals/about.html', {'menu':menu, 'title': 'Главная страница'})
def home(request):
    return render(request, 'animals/about.html', {'menu':menu, 'title': 'Главная страница'})


def login(request):
    return HttpResponse ('Вход')
def reristration(request):
    return HttpResponse ('Регистрация')

def show_post(request, post_id):
    post = get_object_or_404(Announcement, slug=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'animals/post.html', context=context)

def show_category(request, cat_id):
    posts = Announcement.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'animals/index.html', context=context)
