from datetime import timedelta, datetime


def randevu_saatleri(calisma_saati):
    saatler = []
    baslangic = calisma_saati.baslangic_saati
    bitis = calisma_saati.bitis_saati
    ogle_baslangic = calisma_saati.ogle_arasi_baslangic
    ogle_bitis = calisma_saati.ogle_arasi_bitis

    while baslangic < bitis:
        if not (ogle_baslangic <= baslangic < ogle_bitis):
            saatler.append(baslangic)
        baslangic = (datetime.combine(datetime.today(), baslangic) + timedelta(minutes=30)).time()

    return saatler
