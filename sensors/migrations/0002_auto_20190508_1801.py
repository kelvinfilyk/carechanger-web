# Generated by Django 2.1.7 on 2019-05-08 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caregroup',
            name='name',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]
