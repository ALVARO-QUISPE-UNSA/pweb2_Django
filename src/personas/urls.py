from django.urls import path
from .views import (
    PersonaCreateView,
    PersonaDeleteView,
    PersonaDetailView,
    PersonaListView,
    PersonaQueryView,
    PersonaUpdateView,
)
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
    path('oldDetail/<int:myID>/', personasShowObjects, name = 'browsing'),
    path('<int:myID>/oldDelete', personasDeleteView, name = 'deleting'),
    path('oldList', personasListView, name = 'listing'),
    path('', PersonaListView.as_view(), name = 'persona-list'),
    path('<int:pk>/', PersonaDetailView.as_view(), name = 'persona-detail'),
    path('create', PersonaCreateView.as_view(), name = 'persona-create'),
    path('<int:pk>/update/', PersonaUpdateView.as_view(), name = 'persona-update'),
    path('<int:pk>/delete/', PersonaDeleteView.as_view(), name='persona-delete'),
    path('query/', PersonaQueryView.as_view(), name='persona-query'),
]
