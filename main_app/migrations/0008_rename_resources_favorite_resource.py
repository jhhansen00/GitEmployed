# Generated by Django 4.0.1 on 2022-01-18 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_favorite_delete_favorites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='resources',
            new_name='resource',
        ),
    ]
