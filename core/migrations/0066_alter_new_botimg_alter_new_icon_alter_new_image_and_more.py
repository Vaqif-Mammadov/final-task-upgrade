# Generated by Django 5.0.6 on 2024-09-17 18:27

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_social_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='botimg',
            field=models.FileField(blank=True, default='', upload_to=core.models.get_upload_to, verbose_name='Alt şəkil'),
        ),
        migrations.AlterField(
            model_name='new',
            name='icon',
            field=models.FileField(upload_to=core.models.get_upload_to, verbose_name='Profil şəkli'),
        ),
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.FileField(upload_to=core.models.get_upload_to, verbose_name='Şəkil'),
        ),
        migrations.AlterField(
            model_name='new',
            name='image_icon',
            field=models.FileField(default='', upload_to=core.models.get_upload_to, verbose_name='Şəkil ikon formasında'),
        ),
        migrations.AlterField(
            model_name='new',
            name='midimg',
            field=models.FileField(blank=True, default='', upload_to=core.models.get_upload_to, verbose_name='Orta şəkil'),
        ),
        migrations.AlterField(
            model_name='new',
            name='topimg',
            field=models.FileField(blank=True, default='', upload_to=core.models.get_upload_to, verbose_name='Üst şəkil'),
        ),
    ]