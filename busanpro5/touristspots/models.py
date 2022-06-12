from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from users.models import User

# Create your models here.
class TouristSpot(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    thema = models.TextField(blank=True)
    address = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    
    def __str__(self):
        return self.name
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB' )
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class FavoriteSpot(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favoritespots_user")
    mytouristspot = models.ForeignKey(TouristSpot, on_delete=models.CASCADE, related_name="favoritespots_spot")

class RecommendModel(models.Model):
    location = models.CharField(max_length=255)
    theme = models.TextField(blank=True)
    score = models.TextField(blank=True)
    group = models.TextField(blank=True)
    age = models.TextField(blank=True)

