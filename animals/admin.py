from django.contrib import admin
from .models import Note,NoteUser
from .forms import NoteUserCreationForm, NoteUserChangeForm
from django.contrib.auth.admin import UserAdmin

#______________admin note______________
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title','id','img', 'user']
    list_display_links = ['title','id']
    search_fields = ['title','place_of_find','user']

admin.site.register(Note, NoteAdmin)

#_____________admin user____________________

class CustomUserAdmin(UserAdmin):
    add_form = NoteUserCreationForm
    form = NoteUserChangeForm
    model = NoteUser
    list_display = ['email', 'username',]

admin.site.register(NoteUser, CustomUserAdmin)



