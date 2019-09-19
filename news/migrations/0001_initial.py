# Generated by Django 2.2.5 on 2019-09-16 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Название новости')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(blank=True, upload_to='news_photos/%Y/%m/%d/', verbose_name='Фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('publish_date', models.DateTimeField(blank=True, default='Value', null=True)),
                ('author_name', models.CharField(max_length=20, verbose_name='Имя автора')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]