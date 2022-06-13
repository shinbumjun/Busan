from django.db import models

# Create your models here.
class detail(models.Model):
    Place = models.CharField("장소", max_length=32, unique=True)
    Theme = models.CharField("테마", max_length=32)
    Address = models.CharField("주소", max_length=100)
    Explanation = models.TextField("설명", max_length=300)
    Image_2 = models.ImageField("이미지2", blank=True, upload_to="images") 

    def __str__(self):
        return self.Place