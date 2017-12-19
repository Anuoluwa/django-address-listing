from django.db import models

# Create your models here.

class Contact(models.Model):
    """
     Model for contact instance.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular contact across whole address book")
    first_name = models.CharField(max_length=100, help_text="Please fill your first name")
    last_name = models.CharField(max_length=100, help_text="Please fill your last name")
    email = models.EmailField(max_length=100, help_text="Please fill your email address")



    def get_absolute_url(self):

        return reverse('contact-detail', args=[str(self.id)])


    def __str__(self):

        return '%s, %s' % (self.last_name, self.first_name, self.email)
