# Generated by Django 3.0.8 on 2022-01-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0005_auto_20220113_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('national_id', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='county',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='County',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
