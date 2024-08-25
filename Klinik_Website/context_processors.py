from .models import ServicePage

def service_pages(request):
    pages = ServicePage.objects.all()
    return {'service_pages': pages}