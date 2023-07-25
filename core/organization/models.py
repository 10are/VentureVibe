from django.db import models
from django_countries.fields import CountryField

class Organization(models.Model):
    BUSINESS_TYPES = (
        ('sole', 'Şahıs'),
        ('large', 'Büyük işletme'),
        ('sme', 'KOBİ'),
        ('ngo', 'STK'),
    )

    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='media/', blank=True, null=True)
    business_type = models.CharField(max_length=10, choices=BUSINESS_TYPES)
    country = CountryField()
    website = models.URLField(max_length=200, blank=True, null=True)
    employee_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name
