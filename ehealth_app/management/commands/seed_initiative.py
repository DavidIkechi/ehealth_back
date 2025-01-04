from django.core.management.base import BaseCommand
from ehealth_app.models import KeyInitiatives

class Command(BaseCommand):
    help = 'Seed key initiatives'

    key_initiatives = [
        {
            "title": "IPCOR Initiative",
            "link": "https://www.ipcor.ie/"
        },
        {
            "title": "Lero Summit in Athlone",
            "link": "https://lero.ie/"
        },
        {
            "title": "HDR UK Prostate Cancer Symposium",
            "link": "https://www.hdruk.ac.uk/hdruk-conference-2024/"
        },
        {
            "title": "BCNI Symposium",
            "link": "https://www.bloodcancers.ie/bloodcancers/newsevents/bcni-blood-cancer-symposium---friday-24th-may-2024.html"
        },
        {
            "title": "Lero Summit in Athlone",
            "link": "https://www.ul.ie/news/five-university-of-limerick-researchers-presented-with-prestigious-lero-awards"
        },
        {
            "title": "OHDSI HDRUK Conference in the UK",
            "link": "https://www.hdruk.ac.uk/hdruk-conference-2024/"
        },
        {
          "title": "European Cancer Patient's Bill of Rights",
          "link": "https://ecpc.org/european-bill-of-cancer-patients-rights/"
        },
        {
          "title": "Bowel Cancer Research Initiative",
          "link": "https://www.huffingtonpost.co.uk/entry/over-300000-people-will-needlessly-die-from-bowel-cancer-by-2035-because-of-research-gaps-charity-warns_uk_5a2e72fce4b069ec48aece15"
        },
        {
          "title": "DATA-CAN",
          "link": "https://www.data-can.org.uk/"
        }
    ]

    def handle(self, *args, **kwargs):
        for initiative in self.key_initiatives:
            # Use the correct field names from the model
            if not KeyInitiatives.objects.filter(title=initiative['title'], url=initiative['link']).exists():
                # Create the record if it doesn't exist
                KeyInitiatives.objects.create(title=initiative['title'], url=initiative['link'])
                self.stdout.write(self.style.SUCCESS(f"Key initiative '{initiative['title']}' created successfully!"))
            else:
                self.stdout.write(f"Key initiative '{initiative['title']}' already exists.")
