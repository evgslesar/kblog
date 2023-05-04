from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, verbose_name="Url категории", unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ["title"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tags(models.Model):
    title = models.CharField(max_length=50, verbose_name="Тег")
    slug = models.SlugField(max_length=50, verbose_name="Url тега", unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ["title"]
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название поста")
    slug = models.SlugField(max_length=255, verbose_name="Url поста", unique=True)
    author = models.CharField(max_length=100, verbose_name="Автор", blank=True)
    content = models.TextField(blank=True, verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    photo = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True, 
                              verbose_name="Фото")
    views = models.IntegerField(default=0, verbose_name="Кол-во просмотров")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, 
                                 related_name="posts", verbose_name="Категория")
    tags = models.ManyToManyField(Tags, blank=True, related_name="posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

