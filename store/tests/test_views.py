from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products


class TestViewResponses(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, title='django test', created_by_id=1,
                               slug='django-test', price='50.00', image='django')
        self.factory = RequestFactory()

    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test Product response status
        """
        response = self.client.get(reverse('store:product_detail', args=['django-test']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Category response status
        """
        response = self.client.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Test homepage HTML
        """
        request = self.factory.get('/')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertEqual(response.status_code, 200)
