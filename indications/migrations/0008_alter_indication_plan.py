# Generated by Django 3.2.4 on 2021-10-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indications', '0007_alter_indication_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indication',
            name='plan',
            field=models.CharField(choices=[('Premium', 'Premium'), ('Free', 'Free'), ('Standard', 'Standard'), ('Basic', 'Basic')], default='Free', max_length=10),
        ),
    ]
