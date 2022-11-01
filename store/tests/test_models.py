from django.test import TestCase

from store.models import Category, Product

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')   #the fields must match our models
    
    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category)) #if data fits or is the rioght type, it should return true. The test runs successfully

    def test_category_model_entry(self):
        """
        Test Category model return name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')

    