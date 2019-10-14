from django.shortcuts import render
import datetime as dt
from django.http import HttpResponse, Http404
from .models import Image,Location
import pyperclip

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
        
        return render(request,"all-photos/search.html", {"message":message, "images":searched})

    else:
        message = 'You have not searched for any image'
        return render(request, 'all-photos/search.html',{"message":message})    

def image(request,id):
    try:
        images= Image.objects.get(id = id)
    except DoesNotExist:
        raise Http404()
    return render(request,'all-photos/image.html',{'image':images}) 

def location(request,location):
    image = Image.filter_by_location(location)
    location = Location.objects.all()
    return render(request,'all-photos/location.html',{'location':location, 'image':image})