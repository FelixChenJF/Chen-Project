from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('SEPage', views.SEPage, name='SEPage'),
    path('courses/detailedCourse/CEpage', views.CEPage, name='CEPage'),
    path('courses/detailedCourse/DSPage', views.DSPage, name='DSPage'),
    path('courses/detailedCourse/SPPage', views.SPPage, name='SPPage'),
    path('courses/detailedCourse/OSPage', views.OSPage, name='OSPage'),
    path('courses/detailedCourse/EDPage', views.EDPage, name='EDPage'),
    path('detailedCourse/technical_terms/', views.technical_terms, name='technical_terms'),
    path('detailedCourse/daily_vocabulary/', views.daily_vocabulary, name='daily_vocabulary'), 
    path('detailedCourse/custom_page/', views.custom_page, name='custom_page'),
]