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
    # ACADEMIC = 'AC'
    # CLUBS = 'CL'
    # ASSOCIATIONS = 'AS'
    # CATEGORY_CHOICES = (
    #     (ACADEMIC, 'Academics'),
    #     (CLUBS, 'Clubs'),
    #     (ASSOCIATIONS, 'Associations'),
    # )
    # category = models.CharField(
    #     max_length=2,
    #     choices=CATEGORY_CHOICES,
    #     default=ACADEMIC,
    # )

    def __str__(self):
        return self.title
