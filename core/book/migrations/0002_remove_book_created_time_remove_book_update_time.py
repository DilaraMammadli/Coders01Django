# Generated by Django 4.2.2 on 2023-06-06 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='book',
            name='update_time',
        ),
    ]