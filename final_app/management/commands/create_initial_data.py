from django.core.management.base import BaseCommand
from final_app.models import MyModel

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **options):
        # Your code to create or insert initial data
        MyModel.objects.create(name='Example')
        self.stdout.write(self.style.SUCCESS('Initial data created successfully'))