from django.forms import ModelForm
from .models import Note, NoteUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#__________note forms______________________
class AddPostNote(ModelForm):
    class Meta:
        model = Note
        fields = ['title','animal_category', 'info', 'place_of_find', 'img']

#___________user forms_______________________

class NoteUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = NoteUser
        fields = ('username', 'email')

class NoteUserChangeForm(UserChangeForm):

    class Meta:
        model = NoteUser
        fields = ('username', 'email')