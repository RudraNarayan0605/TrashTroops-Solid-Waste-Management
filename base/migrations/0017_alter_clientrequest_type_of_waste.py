# Generated by Django 4.2.7 on 2023-12-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_collectorreport_client_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientrequest',
            name='type_of_waste',
            field=models.CharField(choices=[('Plastic', 'Plastic'), ('Paper', 'Paper'), ('Glass', 'Glass'), ('Metal', 'Metal')], max_length=50),
        ),
    ]
