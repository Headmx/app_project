from django.contrib import admin
from .models import Announcement,NoteUser, Type,Details_type,Animal,Location,Comment
from .forms import NoteUserCreationForm, NoteUserChangeForm
from django.contrib.auth.admin import UserAdmin

#______________type note______________
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id','name']
    search_fields = ['id','name']

#______________ditail note______________
class Details_typeAdmin(admin.ModelAdmin):
    list_display = ['id','names']
    list_display_links = ['id','names']
    search_fields = ['id','names']

#______________animal note______________
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id','animal_name','img']
    list_display_links = ['id','animal_name','img']
    search_fields = ['id','animal_name','img']

#______________location note______________
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id','sity','region','district']
    list_display_links = ['id','sity','region','district']
    search_fields = ['id','sity','region','district']

#______________announcement note______________
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['user','id','mail_contacts','phone_contacts','data']
    list_display_links = ['user','id','mail_contacts','phone_contacts','data']
    search_fields = ['user','id','mail_contacts','phone_contacts','data']

#_____________admin user____________________

class CustomUserAdmin(UserAdmin):
    add_form = NoteUserCreationForm
    form = NoteUserChangeForm
    model = NoteUser
    list_display = ['email', 'username',]

#_____________comment user____________________
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','user']
    list_display_links = ['id','user']
    search_fields = ['id','user']


admin.site.register(NoteUser, CustomUserAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Details_type, Details_typeAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Comment, CommentAdmin)




