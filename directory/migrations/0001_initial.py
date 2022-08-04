# Generated by Django 3.2.15 on 2022-08-04 09:01

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('thumbnail', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('bookmarks', models.ManyToManyField(blank=True, related_name='bookmarked_resources', to=settings.AUTH_USER_MODEL)),
                ('upvotes', models.ManyToManyField(blank=True, related_name='upvoted_resources', to=settings.AUTH_USER_MODEL)),
                ('user_added', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources_added', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tags', to='directory.resource')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='directory.resource')),
                ('user_added', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_left', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
