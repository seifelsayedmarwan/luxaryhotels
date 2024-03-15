from django.db import models
from hotels.models import Hotel

# Create your models here.
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    img = models.ImageField(upload_to='rooms-img/')
    float = models.FloatField() #مساحة الغرفه بالامتار المربعه
    booking_link = models.URLField()
    
    class Meta:
        verbose_name = ("room")
        verbose_name_plural = ("rooms")

    def __str__(self):
        return self.name
    
    def get_absoulte_url(self):
        return reversed("room_details", kwargs={"pk", self.pk}) 