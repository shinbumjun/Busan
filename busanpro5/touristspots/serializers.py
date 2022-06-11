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

class MyFavoriteSpotSerializer(serializers.ModelSerializer):
    touristspots = TouristSpotSerializer(many=True)

    class Meta:
        model = FavoriteSpot
        fields = (
            "id",
            "user_id",
            "touristspots"
        )


class FavoriteSpotSerializer(serializers.ModelSerializer):
    touristspots = TouristSpotSerializer(many=True)

    class Meta:
        model = FavoriteSpot
        fields = (
            "id",
            "user_id",
            "touristspots",
        )
        
    # def create(self, validated_data):
    #     touristspots_data = validated_data.pop('touristspots')
    #     order = TouristSpot.objects.create(**validated_data)

    #     for touristspot_data in touristspots_data:
    #         FavoriteSpot.objects.create(order=order, **touristspots_data)
            
    #     return order

