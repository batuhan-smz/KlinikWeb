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


class WorkingHours(models.Model):
    weekday_hours = models.CharField(max_length=50)
    weekend_hours = models.CharField(max_length=50)

    def __str__(self):
        return f"Hafta İçi: {self.weekday_hours}, Hafta Sonu: {self.weekend_hours}"


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    url = models.CharField(max_length=100,default="/home")

    def __str__(self):
        return f"{self.name} ({self.url})"