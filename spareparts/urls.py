from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'spareparts'

urlpatterns = [
    path('detail/<int:id>/', views.detail_view, name='parts_detail'),
    path('index/', views.show_list, name='parts_index'),
    path('selling/part/', views.AddPartsView.as_view(), name='addpart'),
    path('ad/<str:ad>/', views.filter_ad, name='filter-ad'),

]

