# Generated by Django 5.0.6 on 2024-09-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_article_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.AddField(
            model_name='article',
            name='botimage',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Son şəkil'),
        ),
        migrations.AddField(
            model_name='article',
            name='mainimage',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Əsas şəkil'),
        ),
        migrations.AddField(
            model_name='article',
            name='midimage1',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Orta şəkil1'),
        ),
        migrations.AddField(
            model_name='article',
            name='midimage2',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Orta şəkil2'),
        ),
        migrations.AddField(
            model_name='article',
            name='midimage3',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Orta şəkil3'),
        ),
        migrations.AddField(
            model_name='article',
            name='topimage',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Üst şəkil'),
        ),
    ]
