# Generated by Django 3.2.5 on 2021-08-31 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='photo',
            field=models.ImageField(null=True, upload_to='posts/photo'),
        ),
    ]
