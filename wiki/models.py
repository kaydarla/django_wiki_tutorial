from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    contents = models.TextField(blank=True)
    
        
        

