# Generated by Django 4.0.1 on 2022-01-13 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.TextField(max_length=500, null=True),
        ),
    ]