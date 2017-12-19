from django.contrib import admin

# Register your models here.
from .models import Contact

# admin.site.register(Contact)

# Define the admin class
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
    # The fields attribute lists just those fields that are to be displayed on the form, in order.
    fields = ['first_name', 'last_name', 'email']


# Register the admin class with the associated model
admin.site.register(Contact, ContactAdmin)
