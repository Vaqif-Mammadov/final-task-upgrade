# Generated by Django 5.0.6 on 2024-09-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_plan_my_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='price',
        ),
        migrations.AddField(
            model_name='plan',
            name='price_monthly',
            field=models.CharField(default='', max_length=100, verbose_name='Aylıq qiymət'),
        ),
        migrations.AddField(
            model_name='plan',
            name='price_yearly',
            field=models.CharField(default='', max_length=100, verbose_name='İllik qiymət'),
        ),
    ]