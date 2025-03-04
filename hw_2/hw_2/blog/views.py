from django.http import JsonResponse
from .models import Article

def article_list(request):
    articles = list(Article.objects.values())
    return JsonResponse(articles, safe=False)

def article_detail(request, id):
    article = Article.objects.filter(id=id).values().first()
    return JsonResponse(article, safe=False)