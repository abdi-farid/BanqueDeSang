from django import forms

from .models import *


class DonneurForm(forms.ModelForm):
    class Meta:
        model = Donneur
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'blood_type': forms.Select(attrs={'class': 'form-control'}),
            'rh_factor': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'last_donation_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'additional_notes': forms.Textarea(attrs={'class': 'form-control'}),
        }


class StockDeSangForm(forms.ModelForm):
    class Meta:
        model = StockDeSang
        fields = '__all__'
        widgets = {
            'blood_type': forms.Select(attrs={'class': 'form-control'}),
            'rh_factor': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TransfusionForm(forms.ModelForm):
    class Meta:
        model = Transfusion
        fields = '__all__'
        widgets = {
            'donor': forms.Select(attrs={'class': 'form-control'}),
            'recipient': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'blood_type': forms.Select(attrs={'class': 'form-control', 'type': 'tel'}),
            'rh_factor': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'blood_type': forms.Select(attrs={'class': 'form-control'}),
            'rh_factor': forms.Select(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'required_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'additional_notes': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommandeSangForm(forms.ModelForm):
    class Meta:
        model = CommandeSang
        fields = '__all__'
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'blood_type': forms.Select(attrs={'class': 'form-control', 'type': 'tel'}),
            'rh_factor': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PocheDeSangForm(forms.ModelForm):
    class Meta:
        model = CommandeSang
        widgets = {
            'blood_type': forms.Select(attrs={'class': 'form-control', 'type': 'tel'}),
            'rh_factor': forms.Select(attrs={'class': 'form-control'}),
            'bag_number': forms.TextInput(attrs={'class': 'form-control'}),
            'collection_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'donor': forms.Select(attrs={'class': 'form-control'}),
        }
        fields = '__all__'
