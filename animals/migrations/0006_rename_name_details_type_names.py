# Generated by Django 3.2.9 on 2021-12-11 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0005_auto_20211209_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details_type',
            old_name='name',
            new_name='names',
        ),
    ]
