from django.shortcuts import render , get_object_or_404
from blogs.models import *
from .forms import *
from taggit.models import Tag

# Create your views here.
def home(request):
    trending_blogs = Blog.objects.all()

    context={
    'trending_blogs':trending_blogs,
    }
    return render(request,'core/basics/home.html',context)

def blog(request, id, slug):
    blog = get_object_or_404(Blog , id=id , slug=slug)
    blog.views = blog.views + 1
    blog.save()
    quote = Quote.objects.get(id= 1)
    comment = Comment.objects.filter(blog = blog)[:10:-1]
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        comments = request.POST['message']
        if email and name and comments:
            form = NewCommnetForm()
            newCommnet = form.save(commit=False)
            newCommnet.blog = blog
            newCommnet.full_name = name
            newCommnet.comment = comments[:100]
            newCommnet.email = email
            newCommnet.save()

    context = {
    'blog':blog,
    'quote':quote,
    'comments':comment,
    }
    return render(request,'core/basics/blog.html',context)

def category(request, id , slug):
    category  = get_object_or_404(Category, id=id ,slug=slug)
    blogs=  Blog.objects.filter(category = category).order_by('-created_at')
    context = {
    'blogs':blogs,
    'category':category,
    }
    return render(request,'core/basics/cat_filter.html',context)

def tags(request,slug):
    tag = get_object_or_404(Tag, slug = slug)
    blogs = None
    if tag:
        blogs= Blog.objects.filter(tags = tag).order_by('-created_at')
    context={
    'blogs':blogs,
    'category':tag,
    }
    return render(request,'core/basics/cat_filter.html',context)
