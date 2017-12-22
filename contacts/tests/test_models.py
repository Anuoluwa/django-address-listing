from django.test import TestCase

# Create your tests here.
from contacts.models import Contact

class ContactModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Contact.objects.create(first_name='Anu', last_name='Apiti')

    def test_first_name_label(self):
        contact=Contact.objects.get(id=1)
        field_label = contact._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_first_name_max_length(self):
        contact=Contact.objects.get(id=1)
        max_length = contact._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)

    def test_last_name_label(self):
        contact=Contact.objects.get(id=1)
        field_label = contact._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label,'last name')

    def test_last_name_max_length(self):
        contact=Contact.objects.get(id=1)
        max_length = contact._meta.get_field('last_name').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_last_name_comma_first_name(self):
        contact=Contact.objects.get(id=1)
        expected_object_name = '%s, %s' % (contact.last_name, contact.first_name)
        self.assertEquals(expected_object_name,str(contact))

    def test_email_label(self):
        contact=Contact.objects.get(id=1)
        field_label = contact._meta.get_field('email').verbose_name
        self.assertEquals(field_label,'email')

    def test_email_max_length(self):
        contact=Contact.objects.get(id=1)
        max_length = contact._meta.get_field('email').max_length
        self.assertEquals(max_length,100)
