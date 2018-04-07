from django.conf.urls import url
from . import views

app_name = 'feed'

urlpatterns = [
    url(r'^$', views.feed, name = 'feed'),
    url(r'^add_post$', views.add_post, name = 'add_post'),
    url(r'^add_time_table$', views.add_time_table, name = 'add_time_table'),
    url(r'^show_timetable$', views.show_timetable, name = 'show_timetable'),
    url(r'^add_assign_link$', views.add_assign_link, name = 'add_assign_link'),
    url(r'^add_notes_link$', views.add_notes_link, name = 'add_notes_link'),
    url(r'^add_prev_link$', views.add_prev_link, name = 'add_prev_link'),
    url(r'^search_posts$', views.search_posts, name = 'search_posts'),
    url(r'^academics_posts$', views.academics_posts, name = 'academics_posts'),
    url(r'^clubs_and_association_posts$', views.clubs_and_association_posts, name = 'clubs_and_association_posts'),
    url(r'^sports_posts$', views.sports_posts, name = 'sports_posts'),
]