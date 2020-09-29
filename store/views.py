from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello there, globomantics e-comerce store front coming here...")

def detail(request):
    return HttpResponse("Hello there")

@require_http_methods(["GET"])
# @cache_page(900)
def electronics(request):
    items = ("Windows PC", "Apple Mac", "Apple iPhone", "Lenovo", "Samsung", "Google")
    if request.method == 'GET':
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        return render(request, 'store/list.html', {'items': items})
    elif request.method == 'POST':
        return HttpResponseNotFound("POST Not Found")
    