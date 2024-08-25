from django.contrib import admin
from .models import SliderImage, DoctorInfo, ContactInfo, Explanation, WorkingHours, Menu, About, Services, ServicePage

admin.site.register(SliderImage)
admin.site.register(DoctorInfo)
admin.site.register(ContactInfo)
admin.site.register(Explanation)
admin.site.register(WorkingHours)
admin.site.register(Menu)
admin.site.register(About)
admin.site.register(Services)
@admin.register(ServicePage)
class ServicePageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')
