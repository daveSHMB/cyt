from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Strip
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# index page
def index(request):
    all_strips = Strip.objects.all().order_by('-id')
    paginator = Paginator(all_strips, 1)

    page = request.GET.get('page')
    try:
        current_strip = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        current_strip = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        current_strip = paginator.page(paginator.num_pages)

    recent_posts = Post.objects.order_by('pub_date')[:5]
    context_dict = {'current_strip': current_strip,
                    'recent_posts': recent_posts}
    return render(request, 'comic/index.html', context_dict)

def about(request):
    return render(request, 'comic/about.html')
