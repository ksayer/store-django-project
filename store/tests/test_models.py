
from django.test import TestCase

from account.models import UserBase
from store.models import Category, Product


class TestCategories(TestCase):

    def setUp(self) -> None:
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        UserBase.objects.create(user_name='admin')
        self.data1 = Product.objects.create(category_id=1, name='django test', created_by_id=1,
                                            slug='django-test', price='50.00', image='django')

    def test_product_model_entry(self):
        """
        Test Product model data
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django test')
