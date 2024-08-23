# myapp/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ana sayfa için URL yapılandırması
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
