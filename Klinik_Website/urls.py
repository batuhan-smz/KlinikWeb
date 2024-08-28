# myapp/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ana sayfa için URL yapılandırması
    path('home-en', views.home_en, name='home-en'),  # Ana sayfa için URL yapılandırması
    path('about/', views.about, name='about'),
    path('about-en/', views.about_en, name='about-en'),
    path('contact/', views.contact, name='contact'),
    path('contact-en/', views.contact_en, name='contact-en'),
    path('services/<slug:slug>/', views.service_page_detail, name='service_page_detail'),
    path('services-en/<slug:slug>/', views.service_page_detail_en, name='service_page_detail-en'),
    path('randevu-al/', views.randevu_al, name='randevu_al'),
    path('randevu-al-en/', views.randevu_al_en, name='randevu_al-en'),
    path('randevu-basarili/', views.randevu_basarili, name='randevu_basarili-en'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
