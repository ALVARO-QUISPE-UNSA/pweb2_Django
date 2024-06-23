from django.urls import path
from .views import PersonaListView
from personas.views import (
    personaCreateView,
    personasDeleteView,
    personasListView,
    personasShowObjects,
)
app_name = 'personas'
urlpatterns = [
    path('add/', personaCreateView, name='createPersona'),
    path('add/', personaCreateView, name='createPersona'),
    path('<int:myID>/', personasShowObjects, name = 'browsing'),
    path('<int:myID>/delete', personasDeleteView, name = 'deleting'),
    path('oldList', personasListView, name = 'listing'),
    path('', PersonaListView.as_view(), name = 'persona-list'),
]
