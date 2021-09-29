# Generated by Django 3.2.5 on 2021-09-29 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_posts_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('likes_count', models.ManyToManyField(related_name='likes_count', to='posts.Posts')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.posts')),
            ],
        ),
    ]
