from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
'''
def home(request):
    return render(request, "countries/home.html")
'''
class HomeView(TemplateView):
    template_name = 'countries/home.html' 
    '''
    def get(self, request, *args, **kwargs):
        #return HttpResponse('GET request!')
        return render(request, "countries/home.html")
    '''
    def get_context_data(self, *args, **kwargs):
        colombia = {'name':'colombia', 'code': 'CO'}
        usa = {'name':'estados unidos', 'code': 'USA'}
        mexico = {'name':'mexico', 'code': 'MX'}
        countries = [colombia, usa, mexico]
        return {'countries': countries}


    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')

