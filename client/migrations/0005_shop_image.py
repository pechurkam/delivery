# Generated by Django 3.0.4 on 2020-04-26 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20200307_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='image',
            field=models.ImageField(default='https://res.cloudinary.com/glovoapp/w_680,h_240,c_fit,f_auto,q_auto/Products/phfj7p3w7dhjpxzovqk6', upload_to=''),
        ),
    ]
