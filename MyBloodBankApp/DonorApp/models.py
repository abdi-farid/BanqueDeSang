from django.db import models
from django.utils import timezone


class Donneur(models.Model):
    blood_types = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    )

    rh_types = (
        ('+', 'Positive'),
        ('-', 'Negative'),
    )

    first_name = models.CharField('Nom', max_length=100)
    last_name = models.CharField('Prénom', max_length=100)
    address = models.CharField('Adresse', max_length=255)
    phone_number = models.CharField('Mobile', max_length=20)
    blood_type = models.CharField('Type de sang', max_length=2, choices=blood_types)
    rh_factor = models.CharField('RH', max_length=1, choices=rh_types)
    date_of_birth = models.DateField('Date naissance')
    last_donation_date = models.DateField('Dernier date de don', blank=True, null=True)
    additional_notes = models.TextField('Observations', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class StockDeSang(models.Model):
    blood_types = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    )

    rh_types = (
        ('+', 'Positive'),
        ('-', 'Negative'),
    )

    blood_type = models.CharField('Type Sang', max_length=2, choices=blood_types)
    rh_factor = models.CharField('RH', max_length=1, choices=rh_types)
    quantity = models.PositiveIntegerField('Quantité', default=0)

    def __str__(self):
        return f"{self.blood_type}{self.rh_factor} - Quantity: {self.quantity}"


class Transfusion(models.Model):
    donor = models.ForeignKey(Donneur, on_delete=models.CASCADE)
    recipient = models.CharField('Recipient', max_length=100)
    date = models.DateTimeField('Date', default=timezone.now)
    blood_type = models.CharField('Type Sang', max_length=2, choices=Donneur.blood_types)
    rh_factor = models.CharField('RH', max_length=1, choices=Donneur.rh_types)
    quantity = models.PositiveIntegerField('Quantité')

    def __str__(self):
        return f"Transfusion from {self.donor} to {self.recipient}"


class Patient(models.Model):
    blood_types = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    )

    rh_types = (
        ('+', 'Positive'),
        ('-', 'Negative'),
    )

    first_name = models.CharField('Nom', max_length=100)
    last_name = models.CharField('Prénom', max_length=100)
    address = models.CharField('Adresse', max_length=255)
    phone_number = models.CharField('Mobile', max_length=20)
    blood_type = models.CharField('Type Sang', max_length=2, choices=blood_types)
    rh_factor = models.CharField('RH', max_length=1, choices=rh_types)
    date_of_birth = models.DateField('Date naissance')
    required_date = models.DateField('Date requise')
    additional_notes = models.TextField('Observations', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class CommandeSang(models.Model):
    blood_types = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    )

    rh_types = (
        ('+', 'Positive'),
        ('-', 'Negative'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    blood_type = models.CharField('Type Sang', max_length=2, choices=blood_types)
    rh_factor = models.CharField('RH', max_length=1, choices=rh_types)
    quantity = models.PositiveIntegerField('Quantité')
    date = models.DateTimeField('Date', default=timezone.now)

    def __str__(self):
        return f"Blood Order for {self.patient} - {self.blood_type}{self.rh_factor} - Quantity: {self.quantity}"


class PocheDeSang(models.Model):
    blood_types = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    )

    rh_types = (
        ('+', 'Positive'),
        ('-', 'Negative'),
    )

    blood_type = models.CharField('Type Sang', max_length=2, choices=blood_types)
    rh_factor = models.CharField('RH', max_length=1, choices=rh_types)
    bag_number = models.CharField('N° Poche', max_length=20, unique=True)
    collection_date = models.DateField('Date Collection', default=timezone.now)
    expiry_date = models.DateField('Date Expiration')
    donor = models.ForeignKey(Donneur, on_delete=models.CASCADE)

    def __str__(self):
        return f"Blood Bag: {self.bag_number} - {self.blood_type}{self.rh_factor}"
