# Generated by Django 2.0.3 on 2018-04-07 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Faculty',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='faculty', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('department', models.CharField(blank=True, choices=[('---', '---'), ('CSE', 'Computer Science & Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('MECH', 'Mechanical Engineering'), ('MME', 'Metallurgy Engineering'), ('CHE', 'Chemical Engineering'), ('CIVIL', 'Civil Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('BIO', 'Biotechnology')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='student', serialize=False, to=settings.AUTH_USER_MODEL)),
=======
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
>>>>>>> e9e5bc6e3cebb17a73817550d40ff1f0e33b883b
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=10, null=True)),
                ('course', models.CharField(blank=True, choices=[('BTech', 'B.Tech'), ('MTech', 'M.Tech'), ('MCA', 'MCA'), ('MBA', 'MBA'), ('PHD', 'Phd')], max_length=10, null=True)),
                ('branch', models.CharField(blank=True, choices=[('---', '---'), ('CSE', 'Computer Science & Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('MECH', 'Mechanical Engineering'), ('MME', 'Metallurgy Engineering'), ('CHE', 'Chemical Engineering'), ('CIVIL', 'Civil Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('BIO', 'Biotechnology')], max_length=10, null=True)),
                ('year', models.CharField(blank=True, choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th')], max_length=20, null=True)),
            ],
        ),
    ]
