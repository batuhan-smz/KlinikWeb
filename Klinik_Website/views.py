from django.shortcuts import render, get_object_or_404

from Klinik_Website.models import Menu, SliderImage, About, Services, ServicePage, ContactInfo


# Create your views here.

def home(request):
    menu = Menu.objects.all()
    services = Services.objects.all()
    slider = SliderImage.objects.all()
    slider_instance = SliderImage.objects.first()
    sliderheader = slider_instance.header  # Doğru: Bu bir model alanına erişir
    slidercaption = slider_instance.caption
    about_instance = About.objects.first()
    aboutimage = about_instance.image
    aboutheader = about_instance.header  # Doğru: Bu bir model alanına erişir
    aboutcaption = about_instance.caption
    contact_instance = ContactInfo.objects.first()
    contactemail = contact_instance.email
    contactphone = contact_instance.phone
    contactadress = contact_instance.address

    return render(request, 'home.html', {'services': services,'menü': menu, 'slider': slider ,
                                         'sliderheader': sliderheader, 'slidercaption': slidercaption,
                                         'aboutimage': aboutimage,
                                         'aboutheader': aboutheader, 'aboutcaption': aboutcaption,
                                         'contactemail': contactemail, 'contactphone': contactphone,
                                         'contactadress': contactadress,
                                         })
def about(request):
    return render(home(request),context=None)


def contact(request):
    return None

def service_page_detail(request, slug):
    page = get_object_or_404(ServicePage, slug=slug)
    return render(request, 'service_page_detail.html', {'page': page})

