from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def get_post_image_path(instance,filename):
	return 'posts/{0}/{1}'.format(instance.posted_by.name,filename)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.FileField(upload_to='documents/', null=True)
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
    post = models.ForeignKey(Post, default=None)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Semester(models.Model):
    sno = models.IntegerField()
    subjects= models.ForeignKey('Subject', on_delete=models.CASCADE)

class Subject(models.Model):
    subjectid = models.TextField()
    assignments = models.TextField()
    notes = models.TextField()
    prevpapers= models.TextField()

    def __str__(self):
        return self.subjectid