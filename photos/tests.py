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
        self.assertFalse(len(categories)>0)             
