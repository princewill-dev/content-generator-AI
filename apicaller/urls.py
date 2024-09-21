from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test'),
    path('prompt/', views.ask_view, name='ask'),
]
