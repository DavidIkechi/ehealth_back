from django.core.management.base import BaseCommand
from ehealth_app.models import Membership

class Command(BaseCommand):
    help = 'Seed memberships'
    memberships = {
        "Royal College of Physicians of Ireland",
        "Royal College of Pathology, UK",
        "Haematology Association of Ireland (HAI)",
        "American Society of Haematology (ASH)",
        "American Society of Transplantation and Cellular Therapy (ASTCT)"
    }

    def handle(self, *args, **kwargs):
        for membership in self.memberships:
            # add if it does not exist
            if not Membership.objects.filter(title=membership).exists():
                Membership.objects.create(title=membership)
            self.stdout.write(self.style.SUCCESS(f"Membership '{membership}' created successfully!"))
        