from django.db import models


class SliderImage(models.Model):
    image = models.ImageField(upload_to='images/')
    header = models.CharField(max_length=50, blank=True)
    caption = models.CharField(max_length=200,blank=True)
    caption_en = models.CharField(max_length=200,blank=True)


    def __str__(self):
        return f"{self.header} ({self.caption})"


class About(models.Model):
    image = models.ImageField(upload_to='images/')
    header = models.CharField(max_length=50, blank=True)

    caption = models.CharField(max_length=200, blank=True)
    caption_en = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.header


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
        return f"{self.phone} - {self.email}"


class Explanation(models.Model):
    image = models.ImageField(upload_to='explanation_images/')
    header = models.CharField(max_length=50, blank=True)
    text = models.TextField(null=True, blank=True)
    text_en = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    content_en = models.TextField(null=True, blank=True)

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

class Randevu(models.Model):
    ad = models.CharField(max_length=30,null=False,blank=False,default=None)
    soyad = models.CharField(max_length=20,null=False,blank=False,default=None)
    telefon = models.CharField(max_length=11,primary_key=True,default=None)
    e_posta = models.EmailField(null=True, blank=True,default=None)
    tarih = models.DateTimeField()
    saat = models.TimeField()
    basvuru_sebebi = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.tarih} - {self.saat}"


class Services(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/',null=False)
    name = models.CharField(max_length=30, blank=True, null=True)
    name_en = models.CharField(max_length=30, blank=True, null=True)
    url = models.CharField(max_length=100,default="#")
    content = models.TextField(max_length=500, blank=True, null=True)
    content_en = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.url})"

class ServicePage(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200,default=title)
    description = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True,default=description)
    image = models.ImageField(upload_to='service_images/')
    slug = models.SlugField(unique=True)



    def __str__(self):
        return self.title


class SosyalMedya(models.Model):
    instagram = models.CharField(max_length=50,null=True,blank=True)
    facebook = models.CharField(max_length=50,null=True,blank=True)
    youtube = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.instagram


class Contact(models.Model):
    phone = models.CharField(primary_key=True,max_length=11)
    email = models.EmailField()
    name = models.CharField(max_length=50)
    konu = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name