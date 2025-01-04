from django.core.management.base import BaseCommand
from ehealth_app.models import ResearchInterest

class Command(BaseCommand):
    help = 'Seed research interests'
    research_interests = {
        "Federated Data Sharing", "Myeloid Malignancies",
        "Cancer Research", "Machine Learning in Healthcare",
        "Biomedical Imaging", "Software Development",
        "Algorithms", "Functional Genomics",
        "Cancer Transcription Factors", "Integrative Data Analysis",
        "CRISPR Technology", "Epigenetics",
        "Cancer Therapeutics", "Computational Biology",
        "Molecular Diagnostics", "Precision Medicine",
        "Bioinformatics", "Prostate Cancer Biology",
        "Biomarker Discovery", "Treatment Resistance",
        "Molecular Pathways", "Translational Research",
        "Cancer Therapeutics", "Clinical Biomarkers",
        "Cancer Progression", "Therapy Resistance",
        "Precision Medicine", "Digital Health Technologies",
        "Prostate Cancer", "Federated Data Standardization",
        "Machine Learning in Healthcare", "Biomedical Informatics",
        "Cancer Genomics", "Clinical Data Sharing",
        "Cancer Metastasis", "Drug Resistance Mechanisms",
        "Machine Learning in Medicine", "Network Biology",
        "Molecular Systems Biology", "Computational Biology",
        "Cancer Personalized Medicine", "Patient Stratification",
        "Big Data Analytics", "Clinical Decision Support",
        "Cancer Computational Genomics", "Digital Health",
        "Single Cell Genomics", "Spatial Biology",
        "Cancer Genomics", "Algorithm Development",
        "Immune-Oncology", "Genomics Programs",
        "Real World Evidence", "Open Science",
        "Myeloid Malignancies", "Stem Cell Transplantation",
        "Cellular Therapy", "Translational Medicine",
        "Autophagy Research", "Immune System Enhancement",
        "Gene Mutation Analysis", "Differentiation Therapy",
        "Post-transplant Care", "Clinical Research",
        "Malignant Haematology", "Lymphoid Malignancies",
        "Chronic Lymphocytic Leukaemia", "Cancer Genetics",
        "Drug Resistance Studies", "Next Generation Sequencing",
        "Diagnostic Innovation", "AI in Cancer Diagnostics",
        "Clinical Trials", "Translational Research",
        "Survival Analysis", "Bayesian Statistics",
        "Statistical Modelling", "Machine Learning",
        "Clinical Decision Making", "Translational Statistics",
        "Cancer Research"
    }

    def handle(self, *args, **kwargs):
        for research_interest in self.research_interests:
            # add if it does not exist
            if not ResearchInterest.objects.filter(name=research_interest).exists():
                ResearchInterest.objects.create(name=research_interest)
            self.stdout.write(self.style.SUCCESS(f"Research interest '{research_interest}' created successfully!"))