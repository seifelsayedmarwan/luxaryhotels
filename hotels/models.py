from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from areas.models import Area
from destinations.models import Destination
from django.urls import reverse

# Create your models here.
class Hotel(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='hotels-img/')
    description = models.TextField()
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    booking_link = models.URLField()


    class Meta:
        verbose_name = ("hotel")
        verbose_name_plural = ("hotels")

    def __str__(self):
        return self.name
    
    def get_absoulte_url(self):
        return reverse("hotel_details", kwargs={"pk", self.pk}) 