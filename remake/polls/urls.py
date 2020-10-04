from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = 'polls'


urlpatterns = [
    # path('', TemplateView.as_view(template_name='home/main.html')),
    path('', views.index, name='index'),
    # path('', TemplateView.as_view(template_name='polls/index.html')),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('check', views.check, name='check'),
    path('deck/', views.deck, name='deck'),
    path('owner', views.owner, name='owner')
]
