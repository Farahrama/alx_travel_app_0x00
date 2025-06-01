from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings, bookings, and reviews'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):
            listing = Listing.objects.create(
                title=fake.sentence(),
                description=fake.paragraph(),
                price_per_night=random.uniform(50, 500),
                location=fake.city()
            )

            for _ in range(3):
                Booking.objects.create(
                    listing=listing,
                    guest_name=fake.name(),
                    check_in=fake.date_between(start_date='-1y', end_date='today'),
                    check_out=fake.date_between(start_date='today', end_date='+1y')
                )

            for _ in range(2):
                Review.objects.create(
                    listing=listing,
                    reviewer_name=fake.name(),
                    rating=random.randint(1, 5),
                    comment=fake.text()
                )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))
