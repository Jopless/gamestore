# Generated by Django 2.2.5 on 2019-09-16 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='author_name',
        ),
    ]
