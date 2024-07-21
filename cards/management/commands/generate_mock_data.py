import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from cards.models import Address, Household, Individual
from faker import Faker

class Command(BaseCommand):
    help = 'Generates mock data for testing'

    def add_arguments(self, parser):
        parser.add_argument('--households', type=int, default=50, help='Number of households to create')

    def handle(self, *args, **options):
        fake = Faker()
        num_households = options['households']

        # Create a test user if it doesn't exist
        user, created = User.objects.get_or_create(username='tlofreso')
        if created:
            user.set_password('@#$Secure1')
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Created test user: tlofreso'))

        # Generate addresses
        addresses = []
        for _ in range(num_households):
            address = Address.objects.create(
                street=fake.street_address(),
                city=fake.city(),
                state=fake.state(),
                zipcode=fake.zipcode(),
                country=fake.country()
            )
            addresses.append(address)

        self.stdout.write(self.style.SUCCESS(f'Created {len(addresses)} addresses'))

        # Generate households and individuals
        for address in addresses:
            household = Household.objects.create(
                name=f"The {fake.last_name()} Family",
                address=address,
                created_by=user
            )

            # Generate 1 to 5 individuals per household
            num_individuals = random.randint(1, 5)
            for _ in range(num_individuals):
                Individual.objects.create(
                    first_name=fake.first_name(),
                    last_name=household.name.split()[-1],  # Use the family name
                    household=household
                )

        self.stdout.write(self.style.SUCCESS(f'Created {num_households} households with individuals'))
