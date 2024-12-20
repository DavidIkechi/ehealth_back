from django.urls import path, include
from .views import TagListView, PeopleListView, PeopleInformationListView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('tags/', TagListView.as_view(), name='tags-list'),
    path('people/', PeopleListView.as_view(), name='people-list'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('person-info/<slug:slug>/', PeopleInformationListView.as_view(), name='people-information'),
]