# Generated by Django 5.1 on 2024-08-27 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Klinik_Website', '0017_alter_sosyalmedya_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
