from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.list_authors),
    path('me/', views.welcome)
]