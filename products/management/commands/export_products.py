import json
from django.core.management.base import BaseCommand
from products.models import Product
from products.serializers import ProductSerializer

class Command(BaseCommand):
    help = 'Exports all products to a JSON file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output',
            type=str,
            help='Output file path',
            default='products_export.json'
        )

    def handle(self, *args, **options):
        output_file = options['output']
        products = Product.objects.all()
        
        serialized_data = ProductSerializer.serialize_queryset(products)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(serialized_data, f, indent=4)
            
        self.stdout.write(self.style.SUCCESS(f'Successfully exported {len(serialized_data)} products to {output_file}'))
