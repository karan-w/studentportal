# Generated by Django 2.0.3 on 2018-04-03 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20180403_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('AC', 'Academics'), ('CL', 'Clubs'), ('AS', 'Associations'), ('GN', 'General')], default='AC', max_length=2),
        ),
    ]