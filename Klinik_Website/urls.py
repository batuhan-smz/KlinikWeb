# myapp/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ana sayfa için URL yapılandırması
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/<slug:slug>/', views.service_page_detail, name='service_page_detail'),
    path('randevu-al/', views.randevu_al, name='randevu_al'),
    path('randevu-basarili/', views.randevu_basarili, name='randevu_basarili'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
