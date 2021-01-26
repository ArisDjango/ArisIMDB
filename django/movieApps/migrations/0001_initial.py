# Generated by Django 3.1.5 on 2021-01-26 15:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='movies')),
                ('banner', models.ImageField(upload_to='movies_banner')),
                ('category', models.CharField(choices=[('A', 'ACTION'), ('D', 'ACTION'), ('C', 'COMEDY'), ('R', 'ROMANCE')], max_length=1)),
                ('languages', models.CharField(choices=[('EN', 'ENGLISH'), ('GR', 'GERMAN')], max_length=2)),
                ('status', models.CharField(choices=[('RA', 'RECENTLY ADDED'), ('MW', 'MOST WATCHED'), ('TR', 'TOP RATED')], max_length=2)),
                ('cast', models.CharField(max_length=100)),
                ('year_of_production', models.DateField()),
                ('views_count', models.IntegerField(default=0)),
                ('movie_trailer', models.URLField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D', 'DOWNLOAD LINK'), ('W', 'WATCH LINK')], max_length=1)),
                ('link', models.URLField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_watch_link', to='movieApps.movie')),
            ],
        ),
    ]
