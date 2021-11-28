from django.forms import ModelForm
from .models import Note


class AddPostNote(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'   #форма не работает, не добавляется статья
