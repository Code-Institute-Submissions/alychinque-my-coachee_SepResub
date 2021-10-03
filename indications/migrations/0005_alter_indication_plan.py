# Generated by Django 3.2.4 on 2021-10-03 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indications', '0004_alter_indication_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indication',
            name='plan',
            field=models.CharField(choices=[('Free', 'Free'), ('Basic', 'Basic'), ('Premium', 'Premium'), ('Standard', 'Standard')], default='Free', max_length=10),
        ),
    ]
