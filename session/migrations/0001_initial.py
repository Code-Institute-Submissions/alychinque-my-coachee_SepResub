# Generated by Django 3.2.4 on 2021-07-05 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('indications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.IntegerField()),
                ('jornal', models.TextField()),
                ('concluded', models.BooleanField()),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.coach')),
                ('coachee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.coachee')),
                ('indications1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indication1', to='indications.indication')),
                ('indications2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indication2', to='indications.indication')),
                ('indications3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indication3', to='indications.indication')),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.coach')),
                ('coachee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.coachee')),
            ],
        ),
    ]