from rest_framework import serializers

from .models import TouristSpot, FavoriteSpot

class TouristSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristSpot
        fields = (
            "id",
            "name",
            "description",
            "thema",
            "address",
            "get_image",
            "get_thumbnail"
        )


class FavoriteSpotSerializer(serializers.ModelSerializer):
    touristspots = TouristSpotSerializer(many=True)

    class Meta:
        model = FavoriteSpot
        fields = (
            "id",
            "user_id",
            "touristspots",
            "description",
            "thema",
            "address",
            "get_image",
            "get_thumbnail"
        )
