from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Post, Category, Tag, Comment
from .forms import PostForm


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        self.category = self.kwargs.get('category', None)
        self.tag = self.kwargs.get('tag')
        self.query = self.request.GET.get('query')
        if self.category:
            queryset = Post.objects.filter(category__category_text=self.category)
        elif self.tag:
            queryset = Post.objects.filter(tags__tag_text=self.tag)
        elif self.query:
            queryset = Post.objects.filter(Q(headline__icontains=self.query) | Q(markdown_text__icontains=self.query))

        else:
            queryset = Post.objects.all()
        return queryset
    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'

class ArchiveView():
    pass

class BlogLoginView(LoginView):
    template_name = 'blog/login.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '')
        return context


class BlogLogoutView(View):
    def get(self, requests):
        return logout_then_login(requests)

class AddPostView(LoginRequiredMixin, FormView):
    model = Post
    template_name = 'blog/add_post.html'
    form_class = PostForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ArchiveView(ListView):
    model = Post
    template_name = 'blog/archive.html'


class CommentView(FormView):
    model = Comment
    def form_valid(self, form):
        return super().form_valid(form)


