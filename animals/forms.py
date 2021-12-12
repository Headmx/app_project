from django.forms import ModelForm,inlineformset_factory,BaseInlineFormSet
from .models import Announcement, NoteUser,Animal,Type,Details_type,Location
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#__________note forms______________________
class AddType(ModelForm):
    class Meta:
        model = Type
        fields = ('name', )

class AddDetail(ModelForm):
    class Meta:
        model = Details_type
        fields = ('names', )

class AddAnimal(ModelForm):
    class Meta:
        model = Animal
        fields = ('animal_name', 'animal_details', 'img')

class AddLocation(ModelForm):
    class Meta:
        model = Location
        fields = ('sity', 'region', 'district')

class AddAnnouncement(ModelForm):
    class Meta:
        model = Announcement
        fields = ('user', 'mail_contacts', 'phone_contacts')










#___________user forms_______________________

class NoteUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = NoteUser
        fields = ('username', 'email')

class NoteUserChangeForm(UserChangeForm):

    class Meta:
        model = NoteUser
        fields = ('username', 'email')