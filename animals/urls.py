from . import views
from django.urls import path
from animals.api.views import NoteCreate, CommentCreate, ListAnnouncementView, AnnouncementDetailView,ListCommentView
from animals.views import *

urlpatterns = (
    path('create_note', NoteCreate.as_view()),
    path('create_comment', CommentCreate.as_view()),

    path('all_coments', ListCommentView.as_view()),
    path('all/', ListAnnouncementView.as_view()),
    path('all/<int:pk>/', AnnouncementDetailView.as_view()),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add_note/', AddNote.as_view(), name='add_note'),
    #path('login/', views.login, name= 'login'),
    #path('reristration/', views.reristration, name= 'reristration'),
    path('post/<slug:post_slug>/', views.show_post, name='post'), #раскрывает поле "подробнее на глвной странице"
    path('category/<int:cat_id>/', views.show_category, name='kategory'),

    path('all_animals', views.all_animals, name='all_animals'),

)