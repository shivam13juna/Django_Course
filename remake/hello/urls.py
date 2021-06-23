from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = 'hello'


urlpatterns = [
    # path('', views.index, name='index'),
    path('session/', views.session, name='session'),
    path('cookie/', views.cookie, name='cookie'),
    path('', views.visit, name='visit')
]