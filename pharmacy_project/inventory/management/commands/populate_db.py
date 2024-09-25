from django.core.management.base import BaseCommand
from inventory.models import Drug, Order
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating database...')

        # Clear existing data
        Drug.objects.all().delete()
        Order.objects.all().delete()

        # Sample drug data
        drugs = [
            {'name': 'Aspirin', 'description': 'Pain reliever', 'price': 5.99, 'stock': 100},
            {'name': 'Ibuprofen', 'description': 'Anti-inflammatory', 'price': 7.99, 'stock': 80},
            {'name': 'Amoxicillin', 'description': 'Antibiotic', 'price': 15.99, 'stock': 50},
            {'name': 'Lisinopril', 'description': 'Blood pressure medication', 'price': 12.99, 'stock': 75},
            {'name': 'Levothyroxine', 'description': 'Thyroid hormone', 'price': 10.99, 'stock': 60},
            {'name': 'Metformin', 'description': 'Diabetes medication', 'price': 8.99, 'stock': 90},
            {'name': 'Amlodipine', 'description': 'Calcium channel blocker', 'price': 11.99, 'stock': 70},
            {'name': 'Sertraline', 'description': 'Antidepressant', 'price': 14.99, 'stock': 55},
            {'name': 'Gabapentin', 'description': 'Anticonvulsant', 'price': 13.99, 'stock': 65},
            {'name': 'Omeprazole', 'description': 'Proton pump inhibitor', 'price': 9.99, 'stock': 85},
        ]

        # Create drug objects
        created_drugs = []
        for drug_data in drugs:
            drug = Drug.objects.create(**drug_data)
            created_drugs.append(drug)
            self.stdout.write(f'Created drug: {drug.name}')

        # Create sample orders
        for _ in range(50):  # Create 50 sample orders
            drug = random.choice(created_drugs)
            quantity = random.randint(1, 10)
            date_ordered = timezone.now() - timezone.timedelta(days=random.randint(0, 30))
            
            order = Order.objects.create(drug=drug, quantity=quantity, date_ordered=date_ordered)
            self.stdout.write(f'Created order: {order}')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
