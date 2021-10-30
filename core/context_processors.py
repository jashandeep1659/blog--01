from blogs.models import *
from datetime import date , datetime
import datetime
from taggit.models import Tag
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blogs(request):
    today = date.today()
    last_date = today-datetime.timedelta(days= 3)
    trending_blogs = Blog.objects.filter(created_at__date__lte=today, created_at__date__gt = last_date).order_by('-views')
    recent_blogs= Blog.objects.all().order_by('created_at')
    recent_blogs_page = Paginator(recent_blogs, 5)
    page = request.GET.get('page', 1)
    try:
        recent_blogs_pages = recent_blogs_page.page(page)
    except PageNotAnInteger:
        recent_blogs_pages = recent_blogs_page.page(1)
    except EmptyPage:
        recent_blogs_pages = recent_blogs_page.page(recent_blogs_page.num_pages)

    tags =  random.sample(list(Tag.objects.all()), 4)
    category = random.sample(list(Category.objects.filter(id__in = trending_blogs.values('category_id'))),1 )
    about_me  = About_me.objects.get(id =1)
    context = {
    'trending_blogs':trending_blogs,
    'recent_blogs':recent_blogs,
    'tags':tags,
    'categories':category,
    'about_me':about_me,
    'page_obj':recent_blogs_pages,
    }
    return context
