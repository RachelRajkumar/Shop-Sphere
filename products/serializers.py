class CategorySerializer:
    @staticmethod
    def serialize(category):
        if not category:
            return None
        return {
            'id': category.id,
            'name': category.name,
        }

class ProductSerializer:
    @staticmethod
    def serialize(product):
        if not product:
            return None
        return {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': str(product.price),
            'stock': product.stock,
            'category': CategorySerializer.serialize(product.category),
            'image_url': product.image.url if product.image else None,
        }

    @staticmethod
    def serialize_queryset(queryset):
        return [ProductSerializer.serialize(p) for p in queryset]
