# Generated by Django 3.2.4 on 2021-09-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('Movie', 'Movie'), ('Video', 'Video'), ('Book', 'Book'), ('Podcast', 'Podcast'), ('Activity', 'Activity')], max_length=30, verbose_name='Category')),
            ],
        ),
    ]
