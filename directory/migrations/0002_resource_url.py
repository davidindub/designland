# Generated by Django 3.2.15 on 2022-08-04 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='url',
            field=models.TextField(default=''),
        ),
    ]
