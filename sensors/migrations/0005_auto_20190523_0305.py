# Generated by Django 2.1.7 on 2019-05-23 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0004_data_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sensors.Device'),
        ),
    ]
