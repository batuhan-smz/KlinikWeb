from django import forms

from .helpers import randevu_saatleri
from .models import Randevu, CalismaSaati

class RandevuForm(forms.ModelForm):
    saat = forms.ChoiceField()

    class Meta:
        model = Randevu
        fields = ['hasta', 'tarih', 'saat', 'doktor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Kullanıcının seçtiği tarihe göre ilgili günün çalışma saatini alıyoruz.
        gun_adi = self.instance.tarih.strftime('%A')
        calisma_saati = CalismaSaati.objects.filter(gun=gun_adi).first()

        if not calisma_saati:
            self.fields['saat'].choices = []
            self.add_error(None, 'Bu gün için çalışma saati tanımlanmamış.')
        else:
            self.fields['saat'].choices = [
                (saat, saat.strftime('%H:%M')) for saat in randevu_saatleri(calisma_saati)
            ]