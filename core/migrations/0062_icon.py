# Generated by Django 5.0.6 on 2024-09-16 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_new_image_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='', verbose_name='Şəkil')),
                ('name', models.CharField(max_length=100, verbose_name='Adı')),
            ],
        ),
    ]