from django.db import models


class SliderImage(models.Model):
    image = models.ImageField(upload_to='images/')
    header = models.CharField(max_length=50, blank=True)
    caption = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return f"{self.header} ({self.caption})"


class About(models.Model):
    image = models.ImageField(upload_to='images/')
    header = models.CharField(max_length=50, blank=True)
    caption = models.CharField(max_length=200, blank=True)


class DoctorInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=11, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=11,blank=True)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.phone


class Explanation(models.Model):
    image = models.ImageField(upload_to='explanation_images/')
    header = models.CharField(max_length=50, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]  # İlk 50 karakteri göster


class CalismaSaati(models.Model):
    gun = models.CharField(max_length=10)  # Örneğin: 'Pazartesi'
    baslangic_saati = models.TimeField(null=True, blank=True)
    bitis_saati = models.TimeField(null=True, blank=True)
    ogle_arasi_baslangic = models.TimeField(null=True, blank=True)
    ogle_arasi_bitis = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.gun}: {self.baslangic_saati} - {self.bitis_saati}"
class Hasta(models.Model):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    telefon = models.CharField(max_length=15)
    e_posta = models.EmailField()

    def __str__(self):
        return f"{self.ad} {self.soyad}"

class Randevu(models.Model):
    hasta = models.ForeignKey(Hasta, on_delete=models.CASCADE)
    tarih = models.DateField()
    saat = models.TimeField()
    doktor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tarih} - {self.saat} - {self.hasta}"


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    url = models.CharField(max_length=100,default="#")
    submenuname = models.CharField(max_length=15, blank=True, null=True)
    submenuurl = models.CharField(max_length=100,default="#")
    submenucontent = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.url})"

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/',null=False)
    name = models.CharField(max_length=15, blank=True, null=True)
    url = models.CharField(max_length=100,default="#")
    content = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.url})"

class ServicePage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title