# Generated by Django 2.2.28 on 2023-03-13 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('what_the_book', '0011_book_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
    ]
