from django.test import TestCase
from django.urls import reverse
from .models import CV, ContactInfo


class CVViewsTest(TestCase):
    def setUp(self):
        contact = ContactInfo.objects.create(
            email='jane@example.com',
            phone='1234567890',
        )
        self.cv = CV.objects.create(
            firstname='Jane',
            lastname='Doe',
            bio='Experienced software developer.',
            contacts=contact
        )

    def test_cv_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cv.firstname)
        self.assertTemplateUsed(response, 'home.html')

    def test_cv_view(self):
        response = self.client.get(reverse('cv', args=[self.cv.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cv.bio)
        self.assertTemplateUsed(response, 'cv.html')

    def test_cv_not_found(self):
        response = self.client.get(reverse('cv', args=[999]))
        self.assertEqual(response.status_code, 404)
