from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to= '/')
    img_name = models.CharField(max_length=60)
    img_description = models.CharField(max_length=60)
    
    def save_image():
        pass
        
    def delete_image():
        pass
        
    def update_image():
        pass
    
    def get_image_by_id(id):
        pass
    
    def search_image(category):
        pass
    
    def filter_by_location(location):
        pass            
    
class Location(models.Model):
    pass
class Category(models.Model):  
    pass      