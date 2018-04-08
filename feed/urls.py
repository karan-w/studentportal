from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

app_name = 'feed'

urlpatterns = [
    url(r'^$', views.feed, name = 'feed'),
    url(r'^add_post$', views.add_post, name='add_post'),
    url(r'^search_posts$', views.search_posts, name = 'search_posts'),
    url(r'^academics_posts$', views.academics_posts, name = 'academics_posts'),
    url(r'^update_timetable$', views.update_timetable, name = 'update_timetable'),
    url(r'^clubs_and_association_posts$', views.clubs_and_association_posts, name = 'clubs_and_association_posts'),
    url(r'^sports_posts$', views.sports_posts, name = 'sports_posts'),
    url(r'^add_material$', views.add_material, name = 'add_material'),
    url(r'^assignments/(?P<course_id>\d+)/$', views.view_assignments, name = 'view_assignments'),
    url(r'^notes/(?P<course_id>\d+)/$', views.view_notes, name = 'view_notes'),
    url(r'^previous_papers/(?P<course_id>\d+)/$', views.view_previous_papers, name = 'view_previous_papers'),
    url(r'^feed/subjects.html', views.show_material,name="show_material"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)