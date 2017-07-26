from django.shortcuts import render
from .models import blog
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.
def home(request):
    return HttpResponse('Hello')

# display article page
def detail(request, id):
    try:
        article = blog.objects.get(id=str(id))
    except blog.DoesNotExist:
        raise Http404
    template = loader.get_template('article.html')
    context = {
            'article': article,
            }
    return HttpResponse(template.render(context, request))

# Homepage
def index(request):
    blog_list = blog.objects.all()
    template = loader.get_template('index.html')
    context = {
            'blog_list': blog_list,
            }
    return HttpResponse(template.render(context, request))

