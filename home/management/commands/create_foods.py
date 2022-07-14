from django.core.management.base import BaseCommand, CommandError

from home.models import Food

import ijson


class Command(BaseCommand):
    help = 'Create foods from the given file'

    def add_arguments(self, parser):
        parser.add_argument('foods_json', type=str)

    def handle(self, *args, **options):
        failed = 0
        created = 0
        with open(options['foods_json'], "rb") as f:
            for food in ijson.items(f, 'BrandedFoods.item'):
                try:
                    nutrients = food['labelNutrients']
                    if Food.objects.filter(name=food['description'].lower()).exists():
                        continue
                    Food.objects.create(name=food['description'].lower(), calories=nutrients['calories']['value'],
                                        protein=nutrients['protein']['value'],
                                        carbohydrate=nutrients['carbohydrates']['value'],
                                        total_fats=nutrients['fat']['value'],
                                        serving_size=food['servingSize']

                                        )
                    created += 1
                except Exception as e:
                    failed += 1
                    print(e)
        print(f"Created {created} items failed on {failed} items")
