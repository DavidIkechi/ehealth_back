from django.core.management.base import BaseCommand
from ehealth_app.models import (
    People, ResearchInterest, SocialPlatform, PeopleSocialLink,
    AreaOfExpertise, KeyResearchArea, roleBadge, PeopleInformation
)


class Command(BaseCommand):
    help = 'Add additional information for Dr. Simon McDade'

    def handle(self, *args, **kwargs):
        # Data from JSON-like structure
        profile = {
            "name": "Simon McDade",
            "image": "simonmcdade.png",
            "institution": {
                "title": "Reader",
                "location": "Patrick G Johnston Centre for Cancer Research, Queens University, Belfast"
            },
            "role_badges": ["Project Supervisor", "Belfast", "QUB"],
            "bio": [
                "Dr Simon McDade is a Reader at the Patrick G Johnston Centre for Cancer Research, Queens University Belfast, where he leads the Functional Genomics (FGG) laboratory. His research combines cutting-edge genomic technologies with innovative data analysis approaches to develop novel treatment strategies for cancer patients.",
                "At the forefront of cancer genomics research, Dr McDade's laboratory specializes in utilizing a comprehensive range of genomic technologies including RNA-seq, ChIP-seq, and CRISPR screening. This work is complemented by the development of sophisticated integrative data analysis tools, bridging the gap between complex genomic data and clinical applications.",
                "Dr McDade's research particularly focuses on understanding transcription factor dysfunction in cancer, with special emphasis on the p53 family. His team's work aims to identify genes and processes altered by mutation or de-regulation that could be exploited for diagnostic or therapeutic purposes. This research spans multiple cancer types, including colorectal, prostate, and squamous cancers.",
                "Under Dr McDade's leadership, the laboratory has developed significant expertise in epigenetic research and computational tool development, including the creation of specialized data analysis and Shiny applications. His team welcomes diverse expertise, from biological sciences to computational analysis, fostering an interdisciplinary approach to cancer research."
            ],
            "research_interests": [
                "Functional Genomics",
                "Cancer Transcription Factors",
                "Integrative Data Analysis",
                "CRISPR Technology",
                "Epigenetics",
                "Cancer Therapeutics",
                "Computational Biology",
                "Molecular Diagnostics",
                "Precision Medicine",
                "Bioinformatics"
            ],
            "research_areas": [
                {
                    "title": "Genomic Technologies",
                    "description": "Utilizing RNA-seq, ChIP-seq, and CRISPR screening to understand cancer mechanisms"
                },
                {
                    "title": "Cancer Biology",
                    "description": "Focus on transcription factor dysfunction in colorectal, prostate, and squamous cancers"
                },
                {
                    "title": "Computational Tools",
                    "description": "Development of data analysis tools and Shiny applications for cancer research"
                }
            ],
            "social_links": [
                {"name": "LinkedIn", "url": "https://www.linkedin.com/in/simonmcdade/"},
                {"name": "Google Scholar", "url": "https://scholar.google.co.uk/citations?user=3TXRQVSOwGMC&hl=en"}
            ]
        }

        try:
            # Step 1: Fetch existing person
            person = People.objects.get(full_name=profile['name'])

            # Step 2: Add role badges
            role_badge_objects = [
                roleBadge.objects.get_or_create(name=badge)[0] for badge in profile['role_badges']
            ]

            # Step 3: Add social links
            for link in profile['social_links']:
                platform, _ = SocialPlatform.objects.get_or_create(name=link['name'])
                PeopleSocialLink.objects.get_or_create(
                    people=person,
                    platform=platform,
                    url=link['url']
                )

            # Step 4: Add research interests
            research_interest_objects = [
                ResearchInterest.objects.get_or_create(name=interest)[0]
                for interest in profile['research_interests']
            ]

            # Step 5: Add research areas
            research_area_objects = [
                KeyResearchArea.objects.get_or_create(
                    title=area['title'], description=area['description']
                )[0] for area in profile['research_areas']
            ]

            # Step 6: Update or create PeopleInformation
            people_info, created = PeopleInformation.objects.get_or_create(
                people=person,
                defaults={
                    "about_user": "\n\n".join(profile['bio']),
                    "institution": profile['institution']['location']
                }
            )
            if not created:
                # Update the existing PeopleInformation
                people_info.about_user = "\n\n".join(profile['bio'])
                people_info.institution = profile['institution']['location']
                people_info.save()

            # Step 7: Set many-to-many relationships
            people_info.research_interests.set(research_interest_objects)
            people_info.key_research_areas.set(research_area_objects)
            people_info.role_badge.set(role_badge_objects)

            self.stdout.write(self.style.SUCCESS(f"Successfully updated PeopleInformation for: {profile['name']}"))

        except People.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Person with name {profile['name']} does not exist."))
