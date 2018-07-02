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

class TagsView(TemplateView):
    template_name = 'countries/tags.html' 



