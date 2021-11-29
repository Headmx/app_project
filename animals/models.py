from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


category = (
    ('кошки','КОШКИ'),
    ('собаки', 'СОБАКИ'),
    ('птицы','ПТИЦЫ'),
    ('земноводные','ЗЕМНОВОДНЫЕ'),
    ('иное','ИНОЕ'),
)

class Note (models.Model):
    user = models.ForeignKey('auth.User', verbose_name='имя автора', on_delete=models.CASCADE)
    animal_category = models.CharField('категория животного', choices=category, max_length=50)
    title = models.CharField('заголовок', max_length=50)
    place_of_find = models.CharField ('место найденного животного',max_length=50)
    img = models.ImageField(upload_to='images',null=True, blank=True)
    info = models.TextField('Текст заметки', max_length=1000)
    data = models.DateTimeField('дата публикации заметки')

    def __str__(self):
        return f'заметка {self.id} => статья {self.title}'

    def get_absolut_way(self):
        return reverse ('post', kwargs={'post_id':self.pk}) #метод формирует маршрут post/id статьях на главной странице 'подробнее'

class Comments(models.Model):
    author = models.CharField('комментатор', max_length=50)
    text = models.CharField('текст коммента', max_length=200)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='coments')

    def __str__(self):
        return f'комментатор {self.author} к статье {self.note}'