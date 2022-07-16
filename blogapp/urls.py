from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog-home')
]
