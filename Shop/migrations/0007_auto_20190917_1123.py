# Generated by Django 2.2.5 on 2019-09-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_auto_20190917_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=255),
        ),
    ]