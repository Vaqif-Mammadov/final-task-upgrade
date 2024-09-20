# Generated by Django 5.0.6 on 2024-09-19 16:20

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_alter_new_botimg_alter_new_icon_alter_new_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='botimg',
            field=models.FileField(default='', upload_to=core.models.get_upload_to, verbose_name='Alt şəkil'),
        ),
        migrations.AlterField(
            model_name='new',
            name='midimg',
            field=models.FileField(default='', upload_to=core.models.get_upload_to, verbose_name='Orta şəkil'),
        ),
        migrations.AlterField(
            model_name='new',
            name='topimg',
            field=models.FileField(default='', upload_to=core.models.get_upload_to, verbose_name='Üst şəkil'),
        ),
    ]