from django.db import models

# Create your models here.
class Destination(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='destinations-img/')

    class Meta:
        verbose_name = ("destination")
        verbose_name_plural = ("destinations")

    def __str__(self):
        return self.name
    
    def get_absoulte_url(self):
        return reversed("destination_details", kwargs={"pk", self.pk}) 