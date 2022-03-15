from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestBasketView(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, name='django test1', created_by_id=1,
                               slug='django-test1', price='50.00', image='django')
        Product.objects.create(category_id=1, name='django test2', created_by_id=1,
                               slug='django-test1', price='50.00', image='django')
        Product.objects.create(category_id=1, name='django test3', created_by_id=1,
                               slug='django-test1', price='50.00', image='django')
        self.client.post(
            reverse('basket:basket_add'), data={'productid': 1, 'productqty': 1, 'action': 'post'}, xhr=True)
        self.client.post(
            reverse('basket:basket_add'), data={'productid': 2, 'productqty': 2, 'action': 'post'}, xhr=True)

    def test_basket_url(self):
        """
        Test homepage response status
        """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """
        Test adding products to the basket (ajax)
        """
        response = self.client.post(
            reverse('basket:basket_add'), data={'productid': 3, 'productqty': 1, 'action': 'post'}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4})
        response = self.client.post(
            reverse('basket:basket_add'), data={'productid': 2, 'productqty': 1, 'action': 'post'}, xhr=True)
        self.assertEqual(response.json(), {'qty': 3})

    def test_basket_delete(self):
        """
        Test deleting products from the basket (ajax)
        """
        response = self.client.post(
            reverse('basket:basket_delete'), data={'productid': 2, 'action': 'post'}, xhr=True)
        self.assertEqual(response.json(), {'qty': 1, 'subtotal': '50.00'})

    def test_basket_update(self):
        """
        Test updating products from the basket (ajax)
        """
        response = self.client.post(
            reverse('basket:basket_update'), data={'productid': 2, 'productqty': 1, 'action': 'post'}, xhr=True)
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '100.00'})
