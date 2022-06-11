from .models import Board
from users.serializers import UserSerializer
from rest_framework import serializers


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = [
            "id",
            "author_name",
            "title",
            "content",
            "dt_created",
            "dt_modified",
            "readcnt",
        ]

    author_name = serializers.SerializerMethodField("get_authors_name")

    def get_authors_name(self, obj):
        return obj.author.name


class BoardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = [
            "id",
            "author_name",
            "title",
            "content",
            "dt_created",
            "dt_modified",
            "readcnt",
        ]

    author_name = serializers.SerializerMethodField("get_authors_name")

    def get_authors_name(self, obj):
        return obj.author.name