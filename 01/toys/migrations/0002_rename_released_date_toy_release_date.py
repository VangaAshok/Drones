# Generated by Django 5.0.7 on 2024-07-17 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toy',
            old_name='released_date',
            new_name='release_date',
        ),
    ]
