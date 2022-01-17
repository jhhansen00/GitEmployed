# Generated by Django 3.2.9 on 2022-01-17 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_resource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='replies',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=140)),
                ('comment_date', models.DateField(verbose_name='Comment Posted On:')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.resource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-comment_date'],
            },
        ),
    ]