from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    full_address = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.full_address = f"{self.street}, {self.city}, {self.state} {self.zipcode}, {self.country}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_address


class Household(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Individual(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    household = models.ForeignKey(Household, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MailingList(models.Model):
    name = models.CharField(max_length=255)
    households = models.ManyToManyField(Household)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
