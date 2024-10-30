from django.contrib import admin 
from django.urls import path 
from .views import MenuItemsView, SingleMenuItemView

urlpatterns = [
    #path('', views.index, name='index')
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]