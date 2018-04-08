from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    branch_choices = (
        ('---', '---'),
        ('CSE', 'Computer Science & Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('MECH', 'Mechanical Engineering'),
        ('MME', 'Metallurgy Engineering'),
        ('CHE', 'Chemical Engineering'),
        ('CIVIL', 'Civil Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('BIO', 'Biotechnology'),
    )

    course_choices = (
        ('BTech', 'B.Tech'),
        ('MTech', 'M.Tech'),
        ('MCA', 'MCA'),
        ('MBA', 'MBA'),
        ('PHD', 'Phd'),
    )
    years = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='student')

    phone_number = models.CharField(max_length=20, blank=True, null=True)

    registration_number = models.CharField(max_length=10, blank=True, null=True)
    course = models.CharField(max_length=10, choices=course_choices, blank=True, null=True)
    branch = models.CharField(max_length=10, choices=branch_choices, blank=True, null=True)
    year = models.CharField(max_length=20, choices=years, blank=True, null=True)
    section = models.CharField(max_length=2, blank=True, null=True)
    semester = models.IntegerField(null=True)

    def __str__(self):
        return (self.user.username + "_" + self.registration_number)


class Faculty(models.Model):
    branch_choices = (
        ('---', '---'),
        ('CSE', 'Computer Science & Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('MECH', 'Mechanical Engineering'),
        ('MME', 'Metallurgy Engineering'),
        ('CHE', 'Chemical Engineering'),
        ('CIVIL', 'Civil Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('BIO', 'Biotechnology'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='faculty')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=10, choices=branch_choices, blank=True, null=True)
    # teaching = models.ForeignKey

    def __str__(self):
        return (self.user.first_name + "_" + self.user.last_name)
