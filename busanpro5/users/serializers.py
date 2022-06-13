from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
import django.contrib.auth.password_validation as validators
from django.core.exceptions import ValidationError
from django.utils import timezone

User = get_user_model()


# 회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id","email", "name", "password"]
        extra_kwagrs = {
            "password": {"write_only": True},
            "username": {"read_only": True},
        }

    def validate_password(self, value):
        try:
            validators.validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])

        user.is_active = True
        user.save()
        return user


# 로그인
class LoginUserSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            user.last_login = timezone.now()
            user.save(update_fields=["last_login"])
            return user
        raise serializers.ValidationError("Unable to login with provided credentials.")


# 접속 유지 확인
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id", "name","email"]