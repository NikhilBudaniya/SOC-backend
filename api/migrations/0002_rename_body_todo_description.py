# Generated by Django 4.0.5 on 2022-06-27 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='body',
            new_name='description',
        ),
    ]
