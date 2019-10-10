from django.test import TestCase
from .models import Image, Location, Category

class LocationTest(TestCase):
    '''
    a class to test the location instances and its methods
    '''
    def setUp(self):
        self.location = Location(nameloc='kacyiru')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))    
        
    def test_save_location(self):
        '''
        function to check the save method
        '''
        self.location.save_location()
        loc = Location.objects.all()
        self.assertTrue(len(loc)>0) 
        
    def  test_delete_location(self):
        self.location.save_location()
        loc = Location.objects.filter(nameloc = 'kacyiru').first()
        delete = Location.objects.filter(nameloc=loc.nameloc).delete()
        locs = Location.objects.all()
        print(locs)
        self.assertTrue(len(locs)==0)  
        
    def test_update_location(self):
        self.location.save_location()
        loc = Location.objects.filter(nameloc = 'kacyiru').first()
        update = Location.objects.filter(nameloc = loc.nameloc).update(nameloc='gishushu') 
        updated = Location.objects.filter(nameloc = 'gishushu').first()
        self.assertNotEqual(loc.nameloc, updated.nameloc)        

class ImageTest(TestCase):
    '''
    a class to test the Image and it's instances
    '''
    def setUp(self):
        self.picture = Image( image ='image/', img_name='myPicture', img_description='description')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.picture, Image))
        
    def test_save_image(self):
        '''
        function to check save method
        '''
        self.picture.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
        
    def test_delete_image(self):
        '''
        method to delete a saved image
        '''
        self.picture.save_image()
        image = Image.objects.filter(img_name='myPicture').first()
        delete = Image.objects.filter(img_name= image.img_name).delete()
        images = Image.objects.all()
        self.assertFalse(len(images) == 1)    
        
    def test_update_image(self):
        '''
        a method to check the update method
        '''
        self.picture.save_image()
        image = Image.objects.filter(img_name='myPicture').first()
        update = Image.objects.filter(img_name= image.img_name).update(img_name = 'Picta')
        updated = Image.objects.filter(img_name = 'Picta').first()
        self.assertNotEqual(image.img_name, updated.img_name)
              
        
class CategoryTest(TestCase):
    '''
    class to check the instances and function of category model
    '''
    def setUp(self):
        self.cat = Category( namecat ='leisure')    
        
    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))
        
    def test_save_cat(self):
        self.cat.save_cat()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)  
        
    def test_delete_cat(self):
        '''
        method to delete a saved category
        '''
        self.cat.save_cat()
        cat = Category.objects.filter(namecat='leisure').first()
        delete = Category.objects.filter(namecat= cat.namecat).delete()
        catz = Category.objects.all()
        self.assertFalse(len(catz) == 1)    
        
    def test_update_image(self):
        '''
        a method to check the update method
        '''
        self.cat.save_cat()
        cate = Category.objects.filter(namecat='leisure').first()
        update = Category.objects.filter(namecat= cate.namecat).update(namecat='food')
        updated = Category.objects.filter(namecat = 'food').first()
        self.assertNotEqual(cate.namecat, updated.namecat)               
