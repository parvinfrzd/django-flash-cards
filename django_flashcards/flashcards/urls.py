from django.contrib import admin 
from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/',views.about, name='about'),
    path('flashcards/', views.index, name='index'),
    path('flashcards/<int:flashcard_id>', views.detail, name='detail'),
    path('flashcards/new/', views.FlashcardCreate.as_view(), name='new'),
]