# Generated by Django 3.0.6 on 2020-06-04 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0003_auto_20200604_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addition',
            name='first_number',
            field=models.DecimalField(decimal_places=2, default='', max_digits=19),
        ),
        migrations.AlterField(
            model_name='addition',
            name='second_number',
            field=models.DecimalField(decimal_places=2, default='', max_digits=19),
        ),
        migrations.AlterField(
            model_name='addition',
            name='total',
            field=models.DecimalField(decimal_places=2, default='', max_digits=19),
        ),
    ]
