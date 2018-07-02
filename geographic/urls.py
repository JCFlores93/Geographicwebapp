"""geographic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from countries.views import HomeView, TagsView, CountryDetailView,CountryDetailIDView
from continents.views import ContinentsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('tags/', TagsView.as_view(), name="tags"),
    path('continents/', ContinentsView.as_view(), name="continents_home"),
    path('countries/<int:id>/', CountryDetailIDView.as_view(), name="country_id_detail"),
    path('countries/<code>/', CountryDetailView.as_view(), name="country_code_detail")
]
