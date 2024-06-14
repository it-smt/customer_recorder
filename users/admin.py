from django.contrib import admin

from .models import PersonalInformation, WorkingDay, User


@admin.register(PersonalInformation)
class PersonalInformationAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkingDay)
class WorkingDayAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
