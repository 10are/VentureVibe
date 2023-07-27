from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model

User = get_user_model()

class Organization(models.Model):
    BUSINESS_TYPES = (
        ('sole', 'Şahıs'),
        ('large', 'Büyük işletme'),
        ('sme', 'KOBİ'),
        ('ngo', 'STK'),
    )

    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='media/', blank=True, null=True)
    business_type = models.CharField(max_length=10, choices=BUSINESS_TYPES, blank=True, null=True)
    country = CountryField(blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    employee_count = models.PositiveIntegerField(blank=True, null=True)
    like_count = models.PositiveIntegerField(default=0)  # Like sayısı
    dislike_count = models.PositiveIntegerField(default=0)  # Dislike sayısı

    def __str__(self):
        return self.name

class OrganizationRating(models.Model):
    RATING_CHOICES = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=7, choices=RATING_CHOICES)

    class Meta:
        unique_together = ('organization', 'user')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        like_count = OrganizationRating.objects.filter(organization=self.organization, rating='like').count()
        dislike_count = OrganizationRating.objects.filter(organization=self.organization, rating='dislike').count()
        self.organization.like_count = like_count
        self.organization.dislike_count = dislike_count
        self.organization.save()

    def __str__(self):
        return f"{self.user.username} - {self.organization.name} - {self.rating}"
