from django.shortcuts import render
from django.http import HttpResponse

class Flashcard:  # Note that parens are optional if not inheriting from another class
  def __init__(self, category, front, back, creator, likes, known):
    self.category = category
    self.front = front
    self.back = back
    self.creator = creator
    self.likes = likes 
    self.known = known

data = [
  Flashcard('Arrays',
            'What is an array?',
            'An array is a collection of similar data elements stored at contiguous memory locations.',
            'Parvin',0,False),
  Flashcard('Big O Notation', 
            'What is Big O?  ',
            'is written in the form of O(n) where O stands for “order of magnitude” and n represents what we\'re comparing the complexity of a task against.',
            'Parvin',4,False),
  Flashcard('Arrays',
            'What is linked list?',
            'A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.',
            'Parvin',2,True)
]

# Create your views here.
def home (request): 
    return HttpResponse('YO YO PARVIN')

def about(request): 
    return render(request, 'flashcards/about.html')

def index(request): 
    return render (request, 'flashcards/index.html', { 'data': data })