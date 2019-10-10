from django.test import TestCase
from .models import Image, Location, Category

class ImageTest(TestCase):
    '''
    a class to test the Image and it's instances
    '''
    def setUp(self):
        self.picture = Image( image ='', img_name='myPicture', img_description='description')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.picture, Image))
        
    def test_save_image(self):
        '''
        function to check save method
        '''
        self.picture.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)   
        
# class CategoryTest(TestCase):
#     '''
#     class to check the instances and function of category model
#     '''
#     def setUp(self):
#         self.leisure = Category( namecat ='leisure', image ='')    
        
#     def test_instance(self):
#         self.assertTrue(isinstance(self.leisure, Category))
        
#     def test_save_cat(self):
#         self.leisure.save_cat()
#         categories = Category.objects.all()
#         self.assertTrue(len(categories)>0)             
