# Generated by Django 3.1.3 on 2020-12-01 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clone', '0004_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='users',
            name='following',
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('bio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clone.bio')),
                ('followers', models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
