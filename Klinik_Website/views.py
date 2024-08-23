from django.shortcuts import render

from django.views.generic import TemplateView

from Klinik_Website.models import Menu, SliderImage, About


# Create your views here.
# myapp/views.py

def home(request):
    menu = Menu.objects.all()
    slider = SliderImage.objects.all()
    slider_instance = SliderImage.objects.first()
    sliderheader = slider_instance.header  # Doğru: Bu bir model alanına erişir
    slidercaption = slider_instance.caption
    about_instance = About.objects.first()
    aboutimage = about_instance.image
    aboutheader = about_instance.header  # Doğru: Bu bir model alanına erişir
    aboutcaption = about_instance.caption
    return render(request, 'home.html', {'menü': menu, 'slider': slider ,
                                         'sliderheader': sliderheader, 'slidercaption': slidercaption,
                                         'aboutimage': aboutimage,
                                         'aboutheader': aboutheader, 'aboutcaption': aboutcaption})


def about(request):
    return render(home(request),context=None)


def contact(request):
    return None