from django.test import TestCase
from django.test import TestCase, Client
from .models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
# Create your tests here.
    def setUp(self):
        self.tesObj = Item.objects.create(
            name="tes nama",
            amount=1,
            price=77000,
            description="tes description",
            categories="tes categories"
        )
    def test_model_method(self):
        obj = Item.objects.get(id=self.tesObj.id)
        self.assertEqual(obj.name, "tes nama")
        self.assertEqual(obj.amount, 1)
        self.assertEqual(obj.price, 77000)
        self.assertEqual(obj.description, "tes description")
        self.assertEqual(obj.categories, "tes categories")