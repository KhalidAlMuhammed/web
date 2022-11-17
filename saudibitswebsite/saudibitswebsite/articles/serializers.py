from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id' ,'title', 'url', 'author', 'updated_on', 'content', 'created_on', 'status')