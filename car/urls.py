from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from .views import AddCarView

app_name = 'car'

urlpatterns = [
    path('detail/<int:id>/', views.detail_view, name='detail'),
    path('selling/', views.SellingView.as_view(), name='selling'),
    path('selling/car/', AddCarView, name='addcar'),
    url(r'(?P<id>\d+)/favourite_post/$', views.favourite_post, name='favourite_post'),
    path('favourites/', views.post_favourite_list, name='post_favourite_list'),
    url(r'(?P<id>\d+)/compare_post/$', views.compare_post, name='compare_post'),
    path('compare/', views.post_compare_list, name='post_compare_list'),
    path('announcement/', views.my_announcement, name='announcement'),
    path('update-announcement/<int:id>', views.update_announcement, name='update_announcement'),
    path('delete-announcement/<int:id>', views.delete_announcement, name='delete_announcement'),
    path('search_cars', views.search_cars, name='search-cars'),
    path('city/<str:city>/', views.filter_city, name='filter_city'),
    path('body_type/<str:body_type>/', views.filter_type, name='filter-type'),
    path('milage/', views.milage, name='milage'),
    path('year/', views.year, name='year'),
    path('credit/', views.CreditView.as_view(), name='credit'),
    path('insure/', views.InsureView.as_view(), name='insure'),
    path('contact/', views.contact_view, name='contact'),
    path('passenger/', views.filter_minik, name='passenger'),
    path('commercial/', views.filter_ticari, name='commercial'),
    path('moto/', views.filter_moto, name='moto'),

]
