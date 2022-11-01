from django.test import TestCase

from store.models import Category, Product

class TestCategoiesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')
    
    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """

        data = self.data1
        self.assetTrue(isinstance(data, Category))