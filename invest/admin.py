from django.contrib import admin
from .models import Deposit, Profile

# Register your models here.

@admin.register(Deposit)
class DepositModel(admin.ModelAdmin):
    list_display = ('user', 'deposit', 'gateway', 'plan', 'status')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'state', 'city', 'address', 'zip_code')