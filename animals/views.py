from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, Http404
from .models import *
from .forms import AnnouncementForm
from django.conf import settings
from django.views.generic import View


menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'О проекте', 'url_name': 'about'},
        {'title': 'Опубликовать объявление', 'url_name': 'add_note'},
        {'title': 'Войти', 'url_name': 'login'},
        {'title': 'Регистрация', 'url_name': 'signup'}
        ]

class AddNote(View):
    def get(self, request):
        form = AnnouncementForm()
        return render(request, 'animals/test.html', context={'form': form})

    def post(self, request):
        pos_form = AnnouncementForm()
        error = ''
        if request.method == 'POST':
            pos_form = AnnouncementForm(request.POST, request.FILES)
            if pos_form.is_valid():
                pos_form.save()
                if pos_form.cleaned_data.get('img'):   #эта штука должна отвечать за загрузку, но не работает
                    image = Animal(img=request.FILES['img'])
                    image.save()
                    pos_form.image = image
                return redirect('all_animals')
            else:
                error = 'error form'

        data = {'error': error, 'pos_form': pos_form, 'media_url': settings.MEDIA_URL}
        return render(request, 'animals/all_animals.html', data)


def all_animals(request):
    announcement = Announcement.objects.all()
    context = {
        'announcement': announcement,
        'menu': menu,
        'title': 'Пропавшие животные'
    }
    return render(request, 'animals/all_animals.html', context=context)


def about(request):
    return render(request, 'animals/about.html', {'menu': menu, 'title': 'О проекте'})
def home(request):
    return render(request, 'animals/home.html', {'menu': menu, 'title': 'Главная страница'})


#def login(request):
#    return HttpResponse ('Вход')
#def reristration(request):
#    return HttpResponse ('Регистрация')

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
