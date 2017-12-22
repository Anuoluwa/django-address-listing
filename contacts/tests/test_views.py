from django.test import TestCase
# Create your tests here.
from contacts.models import Contact
from django.urls import reverse


class ContactListViewTest(TestCase):

    """
        Test case for the ContactListView
    """


    @classmethod
    def setUpTestData(cls):
        number_of_contacts = 13
        for contact_num in range(number_of_contacts):
            Contact.objects.create(first_name='Anuoluwapo %s' % contact_num, last_name = 'Surname %s' % contact_num, )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/contacts/list/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('contacts'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('contacts'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'contacts/contact_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('contacts'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['contact_list']) == 10)

    def test_lists_all_contacts(self):
        #Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('contacts')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['contact_list']) == 3)


class ContactCreateViewTest(TestCase):


    def setUp(self):
        test_contact = Contact.objects.create(first_name='John', last_name='doe', email='johndoe@gmail.com')



    def test_uses_correct_template(self):
        resp = self.client.get(reverse('contact_create') )
        self.assertEqual( resp.status_code,200)
        self.assertTemplateUsed(resp, 'contacts/contact_form.html')


    def test_redirects_to_detail_view_on_success(self):
        resp = self.client.post(reverse('contact_create'),{'first_name':' Name','last_name':'Surname','email':'johndoe@gmail.com'} )
        self.assertEqual( resp.status_code,302)
        self.assertTrue( resp.url.startswith('/contacts/list/') )
