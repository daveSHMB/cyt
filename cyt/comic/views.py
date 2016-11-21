from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Strip

# index page
def index(request):
    current_strip = Strip.objects.latest('pub_date')
    context_dict = {'current_strip': current_strip}
    return render(request, 'comic/index.html', context_dict)

def about(request):
    recent = Post.objects.order_by('pub_date')[:5]
    return HttpResponse("There will be things about things here")
