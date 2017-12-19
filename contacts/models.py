from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    """
     Model for contact instance.
     Primary key is automatically added
    """
    first_name = models.CharField(max_length=100, help_text="Please fill your first name")
    last_name = models.CharField(max_length=100, help_text="Please fill your last name")
    email = models.EmailField(max_length=100, help_text="Please fill your email address")


    def get_absolute_url(self):

        return reverse('contact-detail', args=[str(self.id)])


    def __str__(self):

        return '%s, %s' % (self.last_name, self.first_name)
