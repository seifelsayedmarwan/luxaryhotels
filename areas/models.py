from django.db import models
from destinations.models import Destination
# Create your models here.
class Area(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='areas-img/')

    class Meta:
        verbose_name = ("area")
        verbose_name_plural = ("areas")

    def __str__(self):
        return self.name
    
    def get_absoulte_url(self):
        return reversed("area_details", kwargs={"pk", self.pk}) 