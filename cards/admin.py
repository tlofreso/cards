from django.contrib import admin
from .models import Address, Household, Individual, MailingList

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'zipcode', 'country')
    search_fields = ('street', 'city', 'state', 'zipcode', 'country')

@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'created_by')
    list_filter = ('created_by',)
    search_fields = ('name',)

class IndividualInline(admin.TabularInline):
    model = Individual
    extra = 1

@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'household')
    list_filter = ('household',)
    search_fields = ('first_name', 'last_name')

@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')
    filter_horizontal = ('households',)
    search_fields = ('name',)