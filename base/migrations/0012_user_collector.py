# Generated by Django 4.2.7 on 2023-12-20 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_clientrequest_alloted'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='collector',
            field=models.BooleanField(default=False),
        ),
    ]
