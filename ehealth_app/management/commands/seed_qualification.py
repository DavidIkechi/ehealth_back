from django.core.management.base import BaseCommand
from ehealth_app.models import Qualification

class Command(BaseCommand):
    help = 'Seed qualifications'
    qualifications = {
       "MB BCh BAO - NUI Galway",
       "MRCPI - Royal College of Physicians of Ireland",
       "FRCPath - Royal College of Pathology, UK",
       "PhD - University College Cork"
    }

    def handle(self, *args, **kwargs):
        for qualification in self.qualifications:
            # add if it does not exist
            if not Qualification.objects.filter(title=qualification).exists():
                Qualification.objects.create(title=qualification)
            self.stdout.write(self.style.SUCCESS(f"Qualification '{qualification}' created successfully!"))