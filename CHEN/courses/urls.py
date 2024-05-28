from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('SEPage', views.SEPage, name='SEPage'),
    path('CEpage', views.CEPage, name='CEPage'),
    path('DSPage', views.DSPage, name='DSPage'),
    path('SPPage', views.SPPage, name='SPPage'),
    path('OSPage', views.OSPage, name='OSPage'),
    path('EDPage', views.EDPage, name='EDPage'),
    path('EDPage/technical_terms/', views.technical_terms, name='technical_terms'),
    path('EDPage/daily_vocabulary/', views.daily_vocabulary, name='daily_vocabulary'), 
    path('EDPage/daily_vocabulary/custom_page/', views.custom_page, name='custom_page'),
]

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('OSPage', views.OSPage, name='OSPage'),
    path('OSPage/OScustom_Page/', views.OScustom_page, name='OSPage'),
]
