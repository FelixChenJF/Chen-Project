from django.urls import path

from CHEN import settings
from . import views
from django.conf.urls.static import static

app_name = 'courses'

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('SEPage', views.SEPage, name='SEPage'),
    path('CEPage', views.CEPage, name='CEPage'),
    path('DSPage', views.DSPage, name='DSPage'),
    path('SPPage', views.SPPage, name='SPPage'),
    path('OSPage', views.OSPage, name='OSPage'),
    path('EDPage', views.EDPage, name='EDPage'),
    path('EDPage/technical_terms/', views.technical_terms, name='technical_terms'),
    path('EDPage/technical_terms/OScustom_Page/', views.OScustom_page, name='OScustom_page'),
    path('EDPage/daily_vocabulary/', views.daily_vocabulary, name='daily_vocabulary'), 
    path('EDPage/daily_vocabulary/custom_page/', views.custom_page, name='custom_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
