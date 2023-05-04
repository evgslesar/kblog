from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import F
from .models import Post, Category, Tags


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()[:2].select_related('category').prefetch_related('tags')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Тестовый сайт"
        return context


class AllPosts(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.all().select_related('category').prefetch_related('tags')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Все статьи"
        return context


class PostsByCategory(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs["slug"]).select_related('category').prefetch_related('tags')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f'Записи из категории {Category.objects.get(slug=self.kwargs["slug"])}'
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'blog/details.html'
    context_object_name = 'post'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class PostsByTag(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False


    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs["slug"]).select_related('category').prefetch_related('tags')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f'Записи по тегу {Tags.objects.get(slug=self.kwargs["slug"])}'
        return context


class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 4


    def get_queryset(self):
        query_txt = self.request.GET.get('q')
        res1 = Post.objects.filter(title__icontains=query_txt).select_related('category').prefetch_related('tags')
        res2 = Post.objects.filter(content__icontains=query_txt).select_related('category').prefetch_related('tags')
        return res1 or res2 
    
    def get_context_data(self, *, object_list=None, **kwargs):
        query_txt = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        context["q"] = f"s={query_txt}&"
        context["title"] = query_txt
        return context
