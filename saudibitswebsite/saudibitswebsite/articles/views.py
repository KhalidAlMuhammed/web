from django.views import generic
from .models import Article
from django.shortcuts import render
from .serializers import ArticleSerializer 
from rest_framework import viewsets                 

# Create your views here.

class ArticleList (generic.ListView):
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'main/index.html'

class ArticleDetail (generic.DetailView):
    model = Article
    template_name = 'main/article_detail.html'

class ArticleView(viewsets.ModelViewSet):  
    serializer_class = ArticleSerializer   
    queryset = Article.objects.all() 