# Generated by Django 5.0.7 on 2024-07-14 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Schools', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='photo',
        ),
    ]
