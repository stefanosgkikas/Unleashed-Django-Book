from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Tag, Startup
from django.template import Context, loader
from django.shortcuts import get_object_or_404

def tag_list(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})

def tag_detail(request, slug):
   	 return render(request, 'organizer/tag_detail.html', {'tag': get_object_or_404(Tag, slug=slug)})

def startup_list(request):
     return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()}) 

def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug=slug)
    return render(request,'organizer/startup_detail.html',{'startup': startup})
    # return render(request, 'organizer/startup_detail.html', {'startup': get_object_or_404(Startup, slug=slug)})  
