# Generated by Django 3.2.9 on 2021-11-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_auto_20211127_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='animals/images/'),
        ),
    ]
