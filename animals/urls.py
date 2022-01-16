from . import views
from django.urls import path
from animals.api.views import *
from animals.views import *
from rest_framework import routers

router = routers.SimpleRouter()

router.register('announcement', AnnouncementViewSet)
urlpatterns = router.urls

urlpatterns = urlpatterns + [

    path('', views.home, name= 'home'),
    path('partner', views.partner, name= 'partner'),
    path('help', views.help, name= 'help'),
    path('about/', views.about, name= 'about'),
    path('add_note/',AddNote.as_view(), name= 'add_note'),
    path('login/', views.login, name= 'login'),
    path('reristration/', views.reristration, name= 'reristration'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    path('cat', views.show_cat, name= 'cat'),
    path('dog', views.show_dog, name= 'dog'),
    path('bird', views.show_bird, name= 'bird'),
    path('other', views.show_other, name= 'other'),
    path('about/partner', views.partner, name= 'partner'),
    path('about/help', views.help, name= 'help'),
    path('add_note/partner', views.partner, name= 'partner'),
    path('add_note/help', views.help, name= 'help'),
    path('add_note/all_animals', views.all_animals, name= 'all_animals'),
    path('about/all_animals', views.all_animals, name= 'all_animals'),

    path('all_animals', views.all_animals, name = 'all_animals'),

    path('add_note/cat', views.show_cat, name= 'cat'),
    path('add_note/dog', views.show_dog, name= 'dog'),
    path('add_note/bird', views.show_bird, name= 'bird'),
    path('add_note/other', views.show_other, name= 'other'),
]