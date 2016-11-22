from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Strip

# index page
def index(request):
    current_strip = Strip.objects.latest('pub_date')
    recent_posts = Post.objects.order_by('pub_date')[:5]
    context_dict = {'current_strip': current_strip,
                    'recent_posts': recent_posts}
    return render(request, 'comic/index.html', context_dict)

def about(request):
    return render(request, 'comic/about.html')
