from django.shortcuts import render, get_object_or_404, redirect

from Klinik_Website.forms import RandevuForm
from Klinik_Website.models import Menu, SliderImage, About, Services, ServicePage, ContactInfo, SosyalMedya, Explanation


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
    sosyalmedya_instance = SosyalMedya.objects.first()
    sosyalmedya_instagram = sosyalmedya_instance.instagram
    sosyalmedya_facebook = sosyalmedya_instance.facebook
    sosyalmedya_youtube = sosyalmedya_instance.youtube

    return render(request, 'home.html', {'services': services,'menü': menu, 'slider': slider,
                                         'sliderheader': sliderheader, 'slidercaption': slidercaption,
                                         'aboutimage': aboutimage,
                                         'aboutheader': aboutheader, 'aboutcaption': aboutcaption,
                                         'contactemail': contactemail, 'contactphone': contactphone,
                                         'contactadress': contactadress, 'sosyalmedya_instagram': sosyalmedya_instagram,
                                         'sosyalmedya_facebook': sosyalmedya_facebook,'sosyalmedya_youtube': sosyalmedya_youtube

                                         })
def about(request):
    explanation_instance: Explanation = Explanation.objects.first()
    explanationheader = explanation_instance.header
    explanationtext = explanation_instance.text
    explanationimage = explanation_instance.image
    explanationcontent = explanation_instance.content
    return render(request, 'about.html', {'explanationheader': explanationheader,
                                          'explanationtext': explanationtext, 'explanationimage': explanationimage,
                                          'explanationcontent': explanationcontent})


def contact(request):
    return None

def service_page_detail(request, slug):
    page = get_object_or_404(ServicePage, slug=slug)
    return render(request, 'service_page_detail.html', {'page': page})

def randevu_al(request):
    if request.method == 'POST':
        form = RandevuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('randevu_basarili')
    else:
        form = RandevuForm()
    return render(request, 'randevu_al.html', {'form': form})


def randevu_basarili(request):
    return render(request, 'randevu_basarili.html')