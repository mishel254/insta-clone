# Generated by Django 3.1.3 on 2020-11-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='imagepost_like', to='clone.Users'),
        ),
    ]
