# Generated by Django 2.2.5 on 2019-09-17 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_auto_20190917_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.CharField(choices=[('Sports', 'Sports'), ('Shooters', 'Shooters'), ('Racing', 'Racing')], max_length=1, null=True),
        ),
    ]
