from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):

    @classmethod
    def setUp(cls):
        cls.icecream = Menu.objects.create(title="IceCream", price=80, inventory=100)
        cls.gateau = Menu.objects.create(title="Gateau", price=90, inventory=50)
    
    def test_get_all(self):
        item = Menu.objects.all()
        self.assertEqual(str(item[0]), "IceCream : 80.00")
        self.assertEqual(str(item[1]), "Gateau : 90.00")

        
