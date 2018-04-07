from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def get_post_image_path(instance,filename):
	return 'posts/{0}/{1}'.format(instance.post.user.username,filename)

def get_material_file_path(instance, filename):
    return 'material/{0}/{1}'.format(instance.subjectid, filename)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    ACADEMIC = 'AC'
    CLUBSANDASSOCIATIONS = 'CA'
    CLASSREPRESENTATIVE = 'CR'
    GENERAL = 'GN'
    SPORTS = 'SP'
    CATEGORY_CHOICES = (
        (ACADEMIC, 'Academics'),
        (CLUBSANDASSOCIATIONS, 'Clubs and Associations'),
        (GENERAL,'General'),
        (CLASSREPRESENTATIVE, 'Class Representative'),
        (SPORTS, 'Sports'),
    )
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=ACADEMIC,
    )

    def __str__(self):
        return self.text

class Photo(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE, related_name='photo')
    file = models.FileField(upload_to=get_post_image_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100, default=None)

class Semester(models.Model):
    sno = models.IntegerField()
    subjects = models.ForeignKey('Course', on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class CourseMaterial(models.Model):
    course = models.ForeignKey(Course, default=None, on_delete=models.CASCADE, related_name='material')
    ASSIGNMENT = 'AS'
    NOTES = 'NO'
    PREVIOUS_PAPERS = 'PP'
    CATEGORY_CHOICES = (
        (ASSIGNMENT, 'Assignment'),
        (NOTES, 'Notes'),
        (PREVIOUS_PAPERS,'Previous Papers'),
    )
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
    )
    file = models.FileField(upload_to=get_material_file_path)

class Timetable(models.Model):
      years = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
    )
    date = models.DateField()
    year = models.CharField(max_length=20, choices=years, blank=True, null=True)
    section = models.CharField(max_length=2, blank=True, null=True)
    course= models.ForeignKey('Course', on_delete=models.CASCADE)
    
    def __str__(self)
        return self.course


