# Generated by Django 3.2.5 on 2021-09-07 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='wesite',
            new_name='website',
        ),
    ]