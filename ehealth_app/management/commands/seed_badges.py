from django.core.management.base import BaseCommand
from ehealth_app.models import roleBadge

class Command(BaseCommand):
    help = 'Seed role badges'

    def handle(self, *args, **kwargs):
        role_badges = [
            "Project Leader",
            "Limerick", "LDCRC",
            "Researcher", "Research Assistant",
            "Research Fellow", "Project Supervisor",
            "Dublin", "UCD"
        ]

        for role_badge in role_badges:
            # add if it does not exist
            if not roleBadge.objects.filter(name=role_badge).exists():
                roleBadge.objects.create(name=role_badge)
            self.stdout.write(self.style.SUCCESS(f"Role badge '{role_badge}' created successfully!")) 

    

            

            