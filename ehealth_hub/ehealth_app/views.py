from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import (
    TagSerializer,
    PeopleSerializer,
    PeopleInformationSerializer
)
from rest_framework.exceptions import NotFound

from .models import (
    Tag, People, PeopleInformation, 
    ResearchInterest, SocialPlatform, 
    PeopleSocialLink, AreaOfExpertise, 
    KeyInitiatives, KeyResearchArea, 
    Qualification, Membership
)


# Create your views here.
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    ordering_fields = ['name']

class PeopleListView(generics.ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    ordering_fields = ['full_name']
    # order by date created
    ordering = ['-created_at']

class PeopleInformationListView(generics.RetrieveAPIView):
    queryset = PeopleInformation.objects.all()
    serializer_class = PeopleInformationSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    # order by date created
    ordering = ['-created_at']

    def get_object(self):
        slug = self.kwargs.get('slug')
        try:
            return PeopleInformation.objects.get(people__slug=slug)
        except PeopleInformation.DoesNotExist:
            raise NotFound(f"No PeopleInformation found for slug: {slug}")