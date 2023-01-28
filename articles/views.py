from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from django.db.models import Q

from articles.models import Article

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()