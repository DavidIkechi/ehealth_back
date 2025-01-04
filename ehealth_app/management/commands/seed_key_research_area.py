from django.core.management.base import BaseCommand
from ehealth_app.models import AreaOfExpertise

class Command(BaseCommand):
    help = 'Seed key research areas'

    area_expertise = {
        "Course Director, MSc in Health Informatics",
        "Project Management & Stakeholder Engagement",
        "User-Centered Design",
        "Interdisciplinary Research Leadership",
        "Industry-Academic Collaboration",
        "Research Methodology Development"
    }

    def handle(self, *args, **kwargs):
        for expertise in self.area_expertise:
            # add if it does not exist
            if not AreaOfExpertise.objects.filter(name=expertise).exists():
                AreaOfExpertise.objects.create(name=expertise)
            self.stdout.write(self.style.SUCCESS(f"Research expertise '{expertise}' created successfully!"))
