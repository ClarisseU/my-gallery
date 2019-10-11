from django.shortcuts import render
import datetime as dt
from django.http import HttpResponse, Http404
from .models import Image,Location

# Create your views here.

def welcome(request):
    images = Image.objects.all()
    
    return render(request, 'welcome.html',{'image':images})

def search_results(request):
    '''
    a view to do the search the image by category
    '''
    if 'image' in request.GET and request.GET["image"]:
        search = request.GET.get('image')
        searched = Image.search_image(search)
        message = f"{search}"
        
        return render(request,"all-photos/search.html", {"message":message, "image":searched})

    else:
        message = 'You have not searched for any image'
        return render(request, 'all-photos/search.html',{"message":message})    

# def image(request,image):
   
#     image= Image.objects.get(image = image)
    
#     return render(request,'all-photos/image.html',{'image':image})    