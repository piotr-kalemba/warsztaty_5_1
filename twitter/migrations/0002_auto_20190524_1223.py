# Generated by Django 2.2 on 2019-05-24 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='student',
            new_name='user',
        ),
    ]