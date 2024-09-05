# Generated by Django 5.0.6 on 2024-09-05 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_contact_adress_alter_contact_mail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='adress',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='tel',
        ),
        migrations.AddField(
            model_name='contact',
            name='adress1',
            field=models.CharField(blank=True, default='[]', max_length=200, verbose_name='Ünvan1'),
        ),
        migrations.AddField(
            model_name='contact',
            name='adress2',
            field=models.CharField(blank=True, default='[]', max_length=200, verbose_name='Ünvan2'),
        ),
        migrations.AddField(
            model_name='contact',
            name='mail1',
            field=models.EmailField(blank=True, default='[]', max_length=254, verbose_name='E-mail1'),
        ),
        migrations.AddField(
            model_name='contact',
            name='mail2',
            field=models.EmailField(blank=True, default='[]', max_length=254, verbose_name='E-mail2'),
        ),
        migrations.AddField(
            model_name='contact',
            name='tel1',
            field=models.CharField(blank=True, default='[]', max_length=100, verbose_name='Telefon1'),
        ),
        migrations.AddField(
            model_name='contact',
            name='tel2',
            field=models.CharField(blank=True, default='[]', max_length=100, verbose_name='Telefon2'),
        ),
    ]