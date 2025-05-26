from django.urls import path, include
from .views import (
    TagListView, PeopleListView, 
    PeopleInformationListView, home, file_view, 
    view_document, view_files, PeopleInformationAllView
)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('api/tags/', TagListView.as_view(), name='tags-list'),
    path('api/people/', PeopleListView.as_view(), name='people-list'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/person-info/<slug:slug>/', PeopleInformationListView.as_view(), name='people-information'),
    path('', home, name='home'),
    path('api/people-all/', PeopleInformationAllView.as_view(), name='people-information-all'),
    path('docs/', view_document, name='docs'),
    path('files/', view_files, name='files'),
    path('file/<slug:slug>/', file_view, name='file_view'),
]