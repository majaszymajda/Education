
from django.contrib.auth import authenticate, password_validation
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers

from users.models import Profile, User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "gender",
            "is_admin",
            "is_company",
            "date_of_birth",
        )


class UserCreateSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
   
    class Meta:
        model = User
        fields = (
            "id",
            "is_active",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "profile",
        )

    @transaction.atomic
    def create(self, validated_data):
        profile = Profile(** validated_data.pop('profile'))
        user = super().create(validated_data)
        user.set_password(validated_data['password'])

        profile.user = user
        profile.save()
    
        return user


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
   
    class Meta:
        model = User
        fields = (
            "id",
            "is_active",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "profile",
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
   
    class Meta:
        model = User
        fields = (
            "id",
            "is_active",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "profile",
        )

    def update():
        pass



class UserPasswordUpdateSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    default_error_messages = {"invalid_password": _("Nieprawidłowe hasło.")}

    def validate_old_password(self, value):
        user = self.context.get("view").get_object()
        if not user.check_password(value):
            self.fail("invalid_password")
        return value

    def validate(self, data):
        if data["new_password"] != data["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": _("Podane hasła nie są zgodne.")}
            )
        password_validation.validate_password(
            data["new_password"], self.context["request"].user
        )
        return data

    def update(self, instance, validated_data):
        instance.update_password(validated_data["new_password"])
        instance.save()
        return instance


