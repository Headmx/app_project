from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


category = (
    ('cat','CAT'),
    ('dog', 'DOG'),
    ('birds','BIRDTS'),
    ('amphibians','AMPHIBIANS'),
    ('others','OTHERS'),
)

class Note (models.Model):
    user = models.ForeignKey(User, verbose_name='имя автора', on_delete=models.CASCADE)
    animal_category = models.CharField('категория животного', choices=category, max_length=50)
    title = models.CharField('заголовок', max_length=50)
    place_of_find = models.CharField ('место найденного животного',max_length=50)
    img = models.ImageField(upload_to='animals/images/',null=True, blank=True)
    info = models.TextField('Текст заметки', max_length=200)
    data = models.DateTimeField('дата публикации заметки')

    def __str__(self):
        return f'заметка {self.id} => статья {self.title}'

class Comments(models.Model):
    author = models.CharField('комментатор', max_length=50)
    text = models.CharField('текст коммента', max_length=200)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='coments')

    def __str__(self):
        return f'комментатор {self.author} к статье {self.note}'