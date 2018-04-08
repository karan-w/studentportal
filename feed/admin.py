from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Post)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Photo)
admin.site.register(CourseMaterial)
admin.site.register(Timetable)