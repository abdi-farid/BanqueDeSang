# Generated by Django 4.2.1 on 2023-05-27 00:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DonorApp', '0005_alter_commandesang_blood_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pochedesang',
            name='bag_number',
            field=models.CharField(max_length=20, unique=True, verbose_name='N° Poche'),
        ),
        migrations.AlterField(
            model_name='pochedesang',
            name='blood_type',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=2, verbose_name='Type Sang'),
        ),
        migrations.AlterField(
            model_name='pochedesang',
            name='collection_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date Collection'),
        ),
        migrations.AlterField(
            model_name='pochedesang',
            name='expiry_date',
            field=models.DateField(verbose_name='Date Expiration'),
        ),
        migrations.AlterField(
            model_name='pochedesang',
            name='rh_factor',
            field=models.CharField(choices=[('+', 'Positive'), ('-', 'Negative')], max_length=1, verbose_name='RH'),
        ),
    ]
