# Generated by Django 5.0.6 on 2024-09-08 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]