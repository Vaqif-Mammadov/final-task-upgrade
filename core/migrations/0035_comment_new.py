# Generated by Django 5.0.6 on 2024-09-08 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_alter_new_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='new',
            field=models.ForeignKey(default='6', on_delete=django.db.models.deletion.CASCADE, to='core.new'),
        ),
    ]
