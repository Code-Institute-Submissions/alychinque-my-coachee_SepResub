# Generated by Django 3.2.4 on 2021-10-03 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_coach_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='plan',
            field=models.CharField(choices=[('Premium', 'Premium'), ('Standard', 'Standard'), ('Free', 'Free'), ('Basic', 'Basic')], max_length=10),
        ),
    ]
