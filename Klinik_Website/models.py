from django.db import models

class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption

class DoctorInfo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.phone

class Explanation(models.Model):
    image = models.ImageField(upload_to='explanation_images/')
    text = models.TextField()

    def __str__(self):
        return self.text[:50]  # İlk 50 karakteri göster

class WorkingHours(models.Model):
    weekday_hours = models.CharField(max_length=50)
    weekend_hours = models.CharField(max_length=50)

    def __str__(self):
        return f"Hafta İçi: {self.weekday_hours}, Hafta Sonu: {self.weekend_hours}"
