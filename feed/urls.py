from django.conf.urls import url
from . import views

app_name = 'feed'

urlpatterns = [
    url(r'^$', views.feed, name = 'feed'),
    url(r'^add_post$', views.add_post, name = 'add_post'),
    url(r'^search_posts$', views.search_posts, name = 'search_posts'),
    url(r'^academics_posts$', views.academics_posts, name = 'academics_posts'),
    url(r'^clubs_and_association_posts$', views.clubs_and_association_posts, name = 'clubs_and_association_posts'),
    url(r'^sports_posts$', views.sports_posts, name = 'sports_posts'),
]