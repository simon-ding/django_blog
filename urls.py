from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^category/(?P<category>[\w-]+)/$',  views.IndexView.as_view(), name='category'),
    url(r'^tag/(?P<tag>\w+)/$', views.IndexView.as_view(), name='tag'),
    url(r'post/(?P<pk>\d+)/', views.PostView.as_view(), name='post'),
    url(r'^login/$', views.BlogLoginView.as_view(), name='login'),
    url(r'^logout/$', views.BlogLogoutView.as_view(), name='logout'),
    url(r'^post/$', views.AddPostView.as_view(), name='post'),
    url(r'^archive/$', views.ArchiveView.as_view(), name="archive"),
    ]
