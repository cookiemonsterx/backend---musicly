# Generated by Django 2.2.2 on 2019-06-26 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Albums',
            new_name='Album',
        ),
    ]