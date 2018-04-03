from django.conf.urls import url
from . import views

app_name = 'feed'

urlpatterns = [
    url(r'^$', views.feed, name = 'feed'),
    url(r'^add_post$', views.add_post, name = 'add_post'),
    url(r'^search_posts$', views.search_posts, name = 'search_posts'),
]