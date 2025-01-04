from django.core.management.base import BaseCommand
from ehealth_app.models import KeyResearchArea

class Command(BaseCommand):
    help = 'Seed key research areas'

    research_areas = [
        {
          "title": "Molecular Control in Cancer",
          "description": "Understanding cell phenotypic plasticity in metastasis and drug resistance to identify molecular 'Achilles' heels' for personalized medicine"
        },
        {
          "title": "Patient Stratification",
          "description": "Developing more effective approaches for cancer patient stratification and treatment pathway optimization"
        },
        {
          "title": "Computational Methods",
          "description": "Generation of novel algorithms and computational workflows for advanced cancer research and treatment"
        },
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
        },
        {
          "title": "Biomarker Discovery and Validation",
          "description": "Leveraging PCRC resources to identify and validate biomarkers for prostate cancer grade and stage, informing treatment strategies"
        },
        {
          "title": "Therapy Resistance Mechanisms",
          "description": "Investigating resistance to androgen ablation therapy and chemotherapy through genomic and bioinformatic approaches"
        },
        {
          "title": "Translational Research",
          "description": "Bridging laboratory discoveries with clinical applications through international collaborations and the Movember Global Action Plan"
        }
    ]

    def handle(self, *args, **options):
        for research_area in self.research_areas:
            # add if it does not exist
            if not KeyResearchArea.objects.filter(title=research_area['title'], description=research_area['description']).exists():
                KeyResearchArea.objects.create(title=research_area['title'], description=research_area['description'])
            self.stdout.write(self.style.SUCCESS(f"Research area '{research_area['title']}' created successfully!"))