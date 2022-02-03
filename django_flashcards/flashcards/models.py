from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model): 
    name = models.CharField(max_length=50)
    
    
class FlashCard(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    front = models.TextField()
    back = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_known = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.front