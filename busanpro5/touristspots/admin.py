from django.contrib import admin

# Register your models here.
from .models import TouristSpot, FavoriteSpot, RecommendModel

admin.site.register(TouristSpot)
admin.site.register(FavoriteSpot)
admin.site.register(RecommendModel)