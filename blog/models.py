from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Post(models.Model): # models.Model es para que Django sepa que es un modelo y que debe guardarlo en una BD
    #Estos son los atributos
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    #Estos son los metodos  
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title        
    