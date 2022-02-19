from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = (('N', 'Not started yet'),('R', 'Not finished'),('F', 'Finished'))
    
class Category(models.Model): 
    name = models.CharField(max_length=50)    
    status = models.CharField(max_length=1, choices=STATUS, default=STATUS[0][0])   
    
    def __str__(self):
        return self.name
    
class FlashCard(models.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE, default=1)
    front = models.TextField()
    back = models.TextField()
    creator = models.CharField(max_length=50)
    is_known = models.BooleanField(default=False)
    
    def __str__(self):
        return self.front
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"flashcard_id": self.pk})
    