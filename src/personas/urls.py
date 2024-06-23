from django.urls import path
from personas.views import (
    personaCreateView,
    personasDeleteView,
    personasListView,
    personasShowObjects,
)
app_name = 'personas'
urlpatterns = [
    path('add/', personaCreateView, name='createPersona'),
    path('<int:myID>/', personasShowObjects, name = 'browsing'),
    path('<int:myID>/delete', personasDeleteView, name = 'deleting'),
    path('', personasListView, name = 'listing'),
]
