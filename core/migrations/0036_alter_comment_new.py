# Generated by Django 5.0.6 on 2024-09-08 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_comment_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='new',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.new'),
        ),
    ]
