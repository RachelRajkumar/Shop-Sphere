from .models import Product, Category
import logging

logger = logging.getLogger(__name__)

class ProductService:
    @staticmethod
    def get_all_products():
        logger.info("Fetching all products")
        return Product.objects.all()
    
    @staticmethod
    def get_active_products():
        # Assuming stock > 0 means active for now
        logger.info("Fetching active products")
        return Product.objects.filter(stock__gt=0)
    
    @staticmethod
    def get_product_by_id(product_id):
        try:
            logger.info(f"Fetching product with ID: {product_id}")
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            logger.warning(f"Product with ID {product_id} not found")
            return None

    @staticmethod
    def filter_by_category(category_name):
        logger.info(f"Filtering products by category: {category_name}")
        return Product.objects.filter(category__name__icontains=category_name)
