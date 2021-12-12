from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class NoteUser(AbstractUser):
    pass

class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Type of animal')

    def __str__(self):
        return f'{self.id} - {self.name}'

class Details_type(models.Model):
    names = models.CharField(max_length=50, verbose_name='Breed of animal')
    name_id = models.ForeignKey(Type, verbose_name='Type of animal', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.names} - {self.name_id}'

class Animal(models.Model):
    animal_name = models.CharField(max_length=50, verbose_name='name of animal')
    animal_details = models.CharField(max_length=300, verbose_name='description of the animal')
    img = models.ImageField(upload_to='images', null=True, blank=True)
    details_type_id = models.ForeignKey(Details_type, verbose_name='Type of animal',on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.animal_name}'

    def get_absolut_way(self):
        return reverse ('post', kwargs={'post_id':self.pk})

class Location(models.Model):
    sity = models.CharField (max_length=20, verbose_name='city')
    region = models.CharField(max_length=30, verbose_name='region')
    district = models.CharField (max_length=30, verbose_name='district')

    def __str__(self):
        return f'{self.id} - {self.sity}'

class Announcement(models.Model):
    user = models.ForeignKey(NoteUser, verbose_name='name of author', on_delete=models.CASCADE,null=True, blank=True)
    animal_id = models.ForeignKey(Animal, verbose_name='animal information',on_delete=models.CASCADE,null=True, blank=True)
    location_id = models.ForeignKey(Location, verbose_name='find place',on_delete=models.CASCADE,null=True, blank=True)
    data = models.DateTimeField('date of publication', default=timezone.now)
    mail_contacts = models.EmailField(max_length=30, verbose_name='your email')
    phone_contacts = models.IntegerField(verbose_name='enter your phone contact')

    def __str__(self):
        return f'{self.user} - {self.mail_contacts} or {self.phone_contacts}'

class Comment(models.Model):
    user = models.ForeignKey(NoteUser, verbose_name='name of author', on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200, verbose_name= 'info of comment')
    announcement_id = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='coments')

    def __str__(self):
        return f'комментатор {self.user} к статье {self.announcement_id}'