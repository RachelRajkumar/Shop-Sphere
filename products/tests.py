from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Category, Product
from .services import ProductService
from .utils import format_price_currency, calculate_discounted_price
from .validators import validate_positive_price, validate_product_stock
from .serializers import CategorySerializer, ProductSerializer

class UtilityTests(TestCase):
    def test_format_price_currency(self):
        self.assertEqual(format_price_currency(10.5), "$10.50")
        self.assertEqual(format_price_currency("20"), "$20.00")
        self.assertEqual(format_price_currency("invalid"), "$0.00")

    def test_calculate_discounted_price(self):
        self.assertEqual(calculate_discounted_price(100, 20), 80.0)
        self.assertEqual(calculate_discounted_price(50, 100), 0.0)
        with self.assertRaises(ValueError):
            calculate_discounted_price(100, -10)
        with self.assertRaises(ValueError):
            calculate_discounted_price(100, 150)

class ValidatorTests(TestCase):
    def test_validate_positive_price(self):
        self.assertIsNone(validate_positive_price(10))
        self.assertIsNone(validate_positive_price(0))
        with self.assertRaises(ValidationError):
            validate_positive_price(-5)

    def test_validate_product_stock(self):
        self.assertIsNone(validate_product_stock(10))
        self.assertIsNone(validate_product_stock(0))
        with self.assertRaises(ValidationError):
            validate_product_stock(-1)

class ServiceTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product1 = Product.objects.create(
            category=self.category, name="Laptop", price=1000, stock=5
        )
        self.product2 = Product.objects.create(
            category=self.category, name="Mouse", price=50, stock=0
        )

    def test_get_all_products(self):
        products = ProductService.get_all_products()
        self.assertEqual(products.count(), 2)

    def test_get_active_products(self):
        active_products = ProductService.get_active_products()
        self.assertEqual(active_products.count(), 1)
        self.assertEqual(active_products.first(), self.product1)

    def test_get_product_by_id(self):
        product = ProductService.get_product_by_id(self.product1.id)
        self.assertEqual(product, self.product1)
        
        non_existent = ProductService.get_product_by_id(999)
        self.assertIsNone(non_existent)

    def test_filter_by_category(self):
        products = ProductService.filter_by_category("Electro")
        self.assertEqual(products.count(), 2)

class SerializerTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Books")
        self.product = Product.objects.create(
            category=self.category, name="Novel", description="A book", price=15.99, stock=10
        )

    def test_category_serializer(self):
        data = CategorySerializer.serialize(self.category)
        self.assertEqual(data["name"], "Books")
        self.assertEqual(data["id"], self.category.id)

    def test_product_serializer(self):
        data = ProductSerializer.serialize(self.product)
        self.assertEqual(data["name"], "Novel")
        self.assertEqual(data["price"], "15.99")
        self.assertEqual(data["category"]["name"], "Books")
