from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),  # This needs to be on the top
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),
]
