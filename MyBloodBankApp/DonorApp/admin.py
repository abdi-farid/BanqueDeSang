from django.contrib import admin

from .forms import *


# Register your models here.


# création de modèle admin pour chacun de mes modèles #
class DonneurAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'blood_type', 'rh_factor')
    list_filter = ('blood_type', 'rh_factor')
    search_fields = ('first_name', 'last_name', 'blood_type', 'rh_factor')
    list_per_page = 5
    fieldsets = (
        ('Informations Personnelles', {
            'fields': ('first_name', 'last_name', 'date_of_birth',),
            'classes': ('bg-dark',),
        }),
        ('Contacts', {
            'fields': ('address', 'phone_number')
        }),
        ('Information Sang', {
            'fields': ('blood_type', 'rh_factor')
        }),
        ('Notes', {
            'fields': ('additional_notes',),
            'classes': ('collapse',),
        }),
    )


class StockDeSangAdmin(admin.ModelAdmin):
    list_display = ('blood_type', 'rh_factor', 'quantity')
    list_filter = ('blood_type', 'rh_factor')
    search_fields = ('blood_type', 'rh_factor')
    list_per_page = 5
    fieldsets = (
        ('Information Stock', {
            'fields': ('blood_type', 'rh_factor', 'quantity',),
        }),

    )


class TransfusionAdmin(admin.ModelAdmin):
    list_display = ('donor', 'recipient', 'date', 'blood_type', 'rh_factor', 'quantity')
    search_fields = ('donor__first_name', 'donor__last_name', 'recipient__first_name', 'recipient__last_name')
    list_per_page = 5

    fieldsets = (
        ('Information Transfusion', {
            'fields': (('donor', 'recipient', 'date'), ('blood_type', 'rh_factor'), 'quantity',)
        }),
    )


class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'blood_type', 'rh_factor', 'required_date', 'phone_number')
    list_filter = ('blood_type', 'rh_factor')
    search_fields = ('first_name', 'last_name', 'blood_type', 'rh_factor', 'date_of_birth', 'phone_number')
    list_per_page = 5

    fieldsets = (
        ('Informations Personnelle', {
            'fields': ('first_name', 'last_name', 'date_of_birth')
        }),
        ('Contacts', {
            'fields': ('address', 'phone_number', 'required_date')
        }),
        ('Information Sang', {
            'fields': ('blood_type', 'rh_factor')
        }),

        ('Observations', {
            'fields': ('additional_notes',),
            'classes': ('collapse',),
        }),
    )
    # pass


class CommandeSangAdmin(admin.ModelAdmin):
    list_display = ('patient', 'blood_type', 'rh_factor', 'quantity')
    list_filter = ('blood_type', 'rh_factor')
    search_fields = ('patient__first_name', 'patient__last_name', 'blood_type', 'rh_factor')
    list_per_page = 5
    fieldsets = (
        ('Patient Information', {
            'fields': ('patient',)
        }),
        ('Blood Information', {
            'fields': ('blood_type', 'rh_factor', 'quantity')
        }),
        ('Date', {
            'fields': ('date',)
        }),
    )


class PocheDeSangAdmin(admin.ModelAdmin):
    list_display = ('bag_number', 'blood_type', 'rh_factor', 'collection_date', 'expiry_date', 'donor')
    list_filter = ('blood_type', 'rh_factor')
    search_fields = ('bag_number', 'blood_type', 'rh_factor', 'donor__first_name', 'donor__last_name')
    list_per_page = 5
    fieldsets = (
        ('Blood Information', {
            'fields': ('bag_number', 'blood_type', 'rh_factor')
        }),
        ('Collection Information', {
            'fields': ('collection_date', 'expiry_date')
        }),
        ('Donor Information', {
            'fields': ('donor',)
        }),
    )


# Enregistrer mes modeles dans le module ADMIN #
admin.site.register(Donneur, DonneurAdmin, form=DonneurForm)
admin.site.register(StockDeSang, StockDeSangAdmin, form=StockDeSangForm)
admin.site.register(Transfusion, TransfusionAdmin, form=TransfusionForm)
admin.site.register(Patient, PatientAdmin, form=PatientForm)
admin.site.register(PocheDeSang, PocheDeSangAdmin, form=PocheDeSangForm)
admin.site.register(CommandeSang, CommandeSangAdmin, form=CommandeSangForm)
