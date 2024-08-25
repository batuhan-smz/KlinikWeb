from django.contrib import admin
from .models import SliderImage, DoctorInfo, ContactInfo, Explanation, Menu, About, Services, ServicePage, Randevu, Hasta, CalismaSaati

admin.site.register(SliderImage)
admin.site.register(DoctorInfo)
admin.site.register(ContactInfo)
admin.site.register(Explanation)
admin.site.register(Menu)
admin.site.register(About)
admin.site.register(Services)
@admin.register(ServicePage)
class ServicePageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')

@admin.register(Randevu)
class RandevuAdmin(admin.ModelAdmin):
    list_display = ('hasta', 'tarih', 'saat', 'doktor')
    list_filter = ('tarih', 'doktor')
    search_fields = ('hasta__ad', 'hasta__soyad', 'doktor')

@admin.register(Hasta)
class HastaAdmin(admin.ModelAdmin):
    list_display = ('ad', 'soyad', 'telefon', 'e_posta')
    search_fields = ('ad', 'soyad', 'telefon', 'e_posta')

@admin.register(CalismaSaati)
class CalismaSaatiAdmin(admin.ModelAdmin):
    list_display = ('gun', 'baslangic_saati', 'bitis_saati', 'ogle_arasi_baslangic', 'ogle_arasi_bitis')