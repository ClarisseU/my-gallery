from django.db import models

# Create your models here.

class Location(models.Model):
   
    nameloc = models.CharField(max_length=60)
   
    
    def __str__(self):
        return self.nameloc
    
    def save_location(self):
        self.save()
    
    def delete_location(slef):
        self.delete()
    
    def update_location(self):
        self.update()

        
class Image(models.Model):
    
    image = models.ImageField('image/', null=True)
    img_name = models.CharField(max_length=60)
    img_description = models.CharField(max_length=60)
    nameloc = models.ForeignKey(Location, null=True)
    
    def __str__(self):
        return self.image
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def update_image(self):
        self.update()
    
    def get_image_by_id(id):
        pass
    
    def search_image(cls,category):
        photos = cls.objects.filter(title__icontains = category)
    
    def filter_by_location(location):
        pass            
    
class Category(models.Model):  
   
    namecat = models.CharField(max_length=60)
    images = models.ManyToManyField(Image)
    
    def __str__(self):
        return self.namecat
    
    def save_cat(self):
        self.delete
    
    def update_cat(self):
        self.update()
    
    def delete_cat(self):
        self.delete()    
        

