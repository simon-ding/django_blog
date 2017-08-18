from markdown import markdown
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    category_text = models.CharField(max_length=100)

    def __str__(self):
        return self.category_text

    class Mata:
        verbose_name_plural = 'categories'

class Tag(models.Model):
    tag_text = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_text


class Post(models.Model):
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    headline = models.CharField(max_length=200)
    markdown_text = models.TextField('markdown content')
    html = models.TextField('html text', editable=False)
    publication_date = models.DateTimeField(editable=False, default=timezone.now)
    modification_date = models.DateTimeField(editable=False)

    def save(self):
        self.modification_date = timezone.now()
        self.html = markdown(self.markdown_text)
        super(self.__class__, self).save()

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('index')

    class Meta:
        ordering = ['-publication_date', ]

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(editable=False, default=timezone.now)
    reply = models.OneToOneField('self', on_delete=models.CASCADE, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


