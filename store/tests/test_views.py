from importlib import import_module
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from django.conf import settings

from account.models import UserBase
from store.models import Category, Product
from store.views import ProductListView


class TestViewResponses(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        UserBase.objects.create(user_name='admin')
        Product.objects.create(category_id=1, name='django test', created_by_id=1,
                               slug='django-test', price='50.00', image='django')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.client.get('/', HTTP_HOST='ewrwe.com')
        self.assertEqual(response.status_code, 400)
        response = self.client.get('/', HTTP_HOST='bookstore.com')
        self.assertEqual(response.status_code, 200)

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
        response = self.client.get(reverse('store:product_all'))
        html = response.content.decode('utf8')
        self.assertIn('<title>BookStore</title>', html)
        self.assertEqual(response.status_code, 200)
