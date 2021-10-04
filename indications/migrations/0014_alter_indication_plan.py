# Generated by Django 3.2.4 on 2021-10-04 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indications', '0013_alter_indication_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indication',
            name='plan',
            field=models.CharField(choices=[('Standard', 'Standard'), ('Premium', 'Premium'), ('Free', 'Free'), ('Basic', 'Basic')], default='Free', max_length=10),
        ),
    ]