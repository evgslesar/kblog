# Generated by Django 4.2 on 2023-04-24 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url категории')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Тег')),
                ('slug', models.SlugField(unique=True, verbose_name='Url тега')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название поста')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url поста')),
                ('author', models.CharField(blank=True, max_length=100, verbose_name='Автор')),
                ('content', models.TextField(blank=True, verbose_name='Содержание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d', verbose_name='Фото')),
                ('views', models.IntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='blog.tags')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
