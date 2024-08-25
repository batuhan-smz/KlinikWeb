# Generated by Django 5.1 on 2024-08-23 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Klinik_Website', '0004_sliderimage_header_alter_sliderimage_caption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='explanation',
            name='hangiresim',
        ),
        migrations.AddField(
            model_name='explanation',
            name='header',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='explanation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]
