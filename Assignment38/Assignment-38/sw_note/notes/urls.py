from django.urls import path
from . import views

urlpatterns = [
    path("", views.NoteCollectionView.as_view()),
    path("<int:pk>/", views.NoteSinglentonView.as_view())
]