from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PLANS = (
    ('starter', 'STARTER PLAN'),
    ('silver', 'SILVER PLAN'),
    ('gold', 'GOLD PLAN'),
    ('vip', 'VIP PLAN'),
    ('vip-platinum', 'VIP PLATINUM PLAN')
)

DEPOSIT_STATUS = (
    ('pending', 'PENDING'),
    ('successful', 'SUCCESSFUL')
)

DEPOSIT_GATEWAY = (
    ('ethereum', 'ETHEREUM'),
    ('bitcoin', 'BITCOIN')
)

"""
class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    
    city = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username
"""

class Profile(models.Model):
    user = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user

class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='deposits')
    deposit = models.DecimalField(decimal_places=2, max_digits=12)
    profit = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    plan = models.CharField(max_length=20, choices=PLANS)
    status = models.CharField(max_length=20, choices=DEPOSIT_STATUS, default='pending')
    gateway = models.CharField(max_length=20, choices=DEPOSIT_GATEWAY, default='ethereum')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
