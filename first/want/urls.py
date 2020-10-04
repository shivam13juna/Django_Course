from django.urls import path, include
from . import views

app_name = 'want'


urlpatterns = [
    path('', views.index, name='homepage'),
    path('my_list/', views.my_list, name='my_list'),
    path('lets_add/', views.lets_add, name='lets_add'),
    path('lets_del/', views.lets_del, name='lets_del'),
    path('lets_update/', views.lets_update, name='lets_update')

]