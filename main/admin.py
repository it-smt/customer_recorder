from django.contrib import admin

from .models import Service, ContactInformation, Client, Record


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass
