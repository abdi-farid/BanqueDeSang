# Generated by Django 4.2.1 on 2023-05-27 00:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DonorApp', '0004_alter_patient_additional_notes_alter_patient_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandesang',
            name='blood_type',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=2, verbose_name='Type Sang'),
        ),
        migrations.AlterField(
            model_name='commandesang',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='commandesang',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Quantité'),
        ),
        migrations.AlterField(
            model_name='commandesang',
            name='rh_factor',
            field=models.CharField(choices=[('+', 'Positive'), ('-', 'Negative')], max_length=1, verbose_name='RH'),
        ),
    ]
