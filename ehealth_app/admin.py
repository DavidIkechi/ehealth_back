from django.contrib import admin
from .models import (
    Tag, People, PeopleInformation, 
    ResearchInterest, SocialPlatform, 
    PeopleSocialLink, AreaOfExpertise,
    KeyInitiatives, KeyResearchArea,
    Qualification, Membership,
    roleBadge
)

# Tag admin
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Display name and created date
    search_fields = ['name']  # Enable search for tags by name
    ordering = ['name']  # Order tags alphabetically


# People admin
@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'created_at')  # Display main fields
    search_fields = ('full_name',)  # Enable search for people's names
    autocomplete_fields = ['tags']  # Enable autocomplete for tags
    prepopulated_fields = {'slug': ('full_name',)}  # Automatically generate slugs
    list_filter = ('title', 'created_at')  # Add filters for title and creation date
    ordering = ['full_name']  # Order by full name
    filter_horizontal = ['tags']  # Add horizontal filter for tags


# PeopleInformation admin
@admin.register(PeopleInformation)
class PeopleInformationAdmin(admin.ModelAdmin):
    list_display = ('people', 'created_at', 'updated_at')  # Display related person and timestamps
    search_fields = ('people__full_name',)  # Enable search for people's names
    autocomplete_fields = ['people', 'research_interests', 
                           'areas_of_expertise', 'key_initiatives',
                           'key_research_areas', 'qualifications', 
                           'memberships', 'role_badge']  # Enable autocomplete for the related person
    readonly_fields = ('created_at', 'updated_at')  # Make timestamps read-only

# ResearchInterest admin
@admin.register(ResearchInterest)
class ResearchInterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  # Display name and timestamps
    search_fields = ['name']
    ordering = ['name']

# SocialPlatform admin
@admin.register(SocialPlatform)
class SocialPlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'created_at', 'updated_at')
    search_fields = ['name']
    ordering = ['name']

# AreaOfExpertise admin
@admin.register(AreaOfExpertise)
class AreaOfExpertiseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ['name']
    ordering = ['name']

# PeopleSocialLink admin
@admin.register(PeopleSocialLink)
class PeopleSocialLinkAdmin(admin.ModelAdmin):
    list_display = ('people', 'platform', 'url', 'created_at')
    search_fields = ('people__full_name', 'platform__name', 'url')
    list_filter = ('platform', 'created_at')
    autocomplete_fields = ['people', 'platform']

# KeyInitiatives admin
@admin.register(KeyInitiatives)
class KeyInitiativesAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at', 'updated_at')
    search_fields = ['title', 'url']
    ordering = ['title']

# KeyResearchArea admin
@admin.register(KeyResearchArea)
class KeyResearchAreaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ['title']
    ordering = ['title']

# Qualification admin
@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ['title']
    ordering = ['title']

# Membership admin
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ['title']
    ordering = ['title']

# roleBadge admin
@admin.register(roleBadge)
class roleBadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ['name']
    ordering = ['name']