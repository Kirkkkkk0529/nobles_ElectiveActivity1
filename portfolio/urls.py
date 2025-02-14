from django.urls import path
from .views import index, about, projects, contact

app_name = "portfolio"

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('contact/', contact, name='contact'),
]
