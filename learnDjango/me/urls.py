from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='first'),
    path('second/', views.second, name='second'),
    path('<int:car_id>/', views.cardetails, name='cardetails'),
    path('signup/', views.signup, name='signup'),
]