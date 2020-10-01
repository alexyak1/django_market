from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib import messages


def index(request):
    return HttpResponse("Hello there, globomantics e-comerce store front coming here...")

def detail(request):
    return HttpResponse("Hello there")

def logout(request):
    try:
        del request.session['customer']
    except KeyError:
        print('Error while loggin out')
    return HttpResponse('You are logged out.')
            

# @require_http_methods(["GET"])
# @cache_page(900)
class ElectronicsView(View):
    def get(self, request):
        items = ("Windows PC", "Apple Mac", "Apple iPhone", "Lenovo", "Samsung", "Google")
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)

        name = "Alex"
        # self.process()
        messages.info(request, 'Customer successfully fethed')
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        if not request.session.has_key('customer'):
            request.session['customer'] = name
            print('session value set')
        response = render(request, 'store/list.html', {'items': items})
        if request.COOKIES.get('visits'):
            value = int(request.COOKIES.get('visits'))
            print('Getting Cookie.')
            response.set_cookie('visits', value + 1)
        else:
            value = 1
            print('Setting Cookie.')
            response.set_cookie('visits', value)

        return response
    


class ElectronicsView2(TemplateView):
    template_name = 'store/list.html'
    def get_context_data(self, **kwargs):
        items = ("Windows PC", "Apple Mac", "Apple iPhone", "Lenovo", "Samsung", "Google")
        context = {'items': items}
        return context

class ElectronicsView3(ListView):
    template_name = 'store/list.html'
    queryset = ("Windows PC", "Apple Mac", "Apple iPhone", "Lenovo", "Samsung", "Google")
    context_object_name = 'items'
    paginate_by = 2