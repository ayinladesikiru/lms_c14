from rest_framework.routers import SimpleRouter, DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)

urlpatterns = router.urls
