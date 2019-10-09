from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to= '/')
    img_name = models.CharField(max_length=60)
    img_description = models.CharField(max_length=60)
    category = models.ForeignKey(Category)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def update_image():
        pass
    
    def get_image_by_id(id):
        pass
    
    def search_image(cls,category):
        photos = cls.objects.filter(title__icontains = category)
    
    def filter_by_location(location):
        pass            
    
class Location(models.Model):
    idloc= models.CharField(max_length=60)
    nameloc = models.CharField(max_length=60)
    images = models.ForeignKey(Image)
    
    def save_location(self):
        self.save()
    
    def delete_location(slef):
        self.delete()
    
    def update_location(self):
        self.update()
    
class Category(models.Model):  
    idcat = models.CharField(max_length=60)
    namecat = models.CharField
    images = 
    
    def save_cat(self):
        self.delete
    
    def update_cat(self):
        self.update()
    
    def delete_cat(self):
        self.delete()    