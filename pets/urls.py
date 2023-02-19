from django.urls import path
from pets.views import PetViews

urlpatterns = [
    path('pets/', PetViews.as_view()),
    path('pets/<int:pet_id>', PetViews.as_view()),
]