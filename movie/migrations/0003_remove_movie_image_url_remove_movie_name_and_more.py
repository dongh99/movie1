# Generated by Django 4.0.6 on 2022-07-30 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_image_url_movie_name_movie_role_delete_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='name',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='role',
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('role', models.CharField(max_length=100, null=True)),
                ('image_url', models.CharField(max_length=100, null=True)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
    ]
