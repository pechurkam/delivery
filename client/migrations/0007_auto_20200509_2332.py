# Generated by Django 3.0.4 on 2020-05-09 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20200509_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
