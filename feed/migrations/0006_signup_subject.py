# Generated by Django 2.0.3 on 2018-04-05 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20180403_2342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('emailid', models.TextField()),
                ('category', models.TextField()),
                ('subjects', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectid', models.TextField()),
                ('assignments', models.TextField()),
                ('notes', models.TextField()),
                ('prevpapers', models.TextField()),
                ('cr', models.BooleanField(default=False)),
            ],
        ),
    ]
