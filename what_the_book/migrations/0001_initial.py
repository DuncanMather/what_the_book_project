# Generated by Django 2.2.28 on 2023-03-24 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('profilePicture', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=20)),
                ('coverPicture', models.ImageField(blank=True, upload_to='images/book_covers/')),
                ('slug', models.SlugField(unique=True)),
                ('addedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='what_the_book.Admin')),
            ],
            options={
                'verbose_name_plural': 'books',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('profilePicture', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('mainText', models.TextField()),
                ('createdOn', models.DateField()),
                ('likes', models.IntegerField(default=0)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='what_the_book.User')),
                ('reviewOf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='what_the_book.Book')),
            ],
            options={
                'verbose_name_plural': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='BookToRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=20)),
                ('readBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='what_the_book.Admin')),
                ('requestedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='what_the_book.User')),
            ],
            options={
                'verbose_name_plural': 'requested books',
            },
        ),
    ]
