# Generated by Django 2.0.3 on 2018-05-29 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.AlterField(
            model_name='city',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]