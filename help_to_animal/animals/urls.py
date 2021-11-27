from . import views
from django.urls import path
from animals.api.views import NoteCreate, CommentsCreate, ListNoteView, NoteDetailView,ListCommentsView

urlpatterns = (
    path('create_note', NoteCreate.as_view()),
    path('create_comment', CommentsCreate.as_view()),

    path('all_coments', ListCommentsView.as_view()),
    path('all/', ListNoteView.as_view()),
    path('all/<int:pk>/', NoteDetailView.as_view()),
)