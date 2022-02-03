from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, FlashCard

# Create your views here.
def home (request): 
    return HttpResponse('YO YO PARVIN')

def about(request): 
    return render(request, 'flashcards/about.html')

def index(request): 
    flashcards = FlashCard.objects.all()
    return render (request, 'flashcards/index.html', { 'flashcards': flashcards })
  
def detail(request,flashcard_id):
      flashcard = FlashCard.objects.get(id=flashcard_id)
      return render(request, 'flashcards/detail.html', {'flashcard': flashcard})
  
def new(request): 
  return render (request, 'flashcards/new.html')