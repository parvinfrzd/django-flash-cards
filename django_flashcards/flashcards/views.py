from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CategoryForm



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
      category_form = CategoryForm
      print(flashcard.id)
      return render(request, 'flashcards/detail.html', {'flashcard': flashcard, 'category_form': category_form})
  
class CategoryCreate(CreateView):
    model = Category 
    fields = '__all__'
    
# class AddBookForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = ('title', 'person',)
#         widgets = {
#             'person': forms.HiddenInput,
#         } 
          
class FlashcardCreate(CreateView): 
    model = FlashCard
    fields = ['front','back','creator','category']
    
    def form_valid(self,form): 
        form.instance.category_id = self.kwargs.get('pk')
        return super(FlashcardCreate, self.form_valid(form))
 
class FlashcardUpdate(UpdateView): 
    model = FlashCard
    fields = ['front','back','is_known']
    
class FlashcardDelete(DeleteView):
    model = FlashCard
    fields = '__all__'
    success_url = '/flashcards/'


    