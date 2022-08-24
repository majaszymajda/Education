

from email.policy import default
from imp import source_from_cache
import profile
from pyexpat import model
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
        # raise Exception
        profile.save()
        # user.save()

        # profile = Profile.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    # gender = serializers.ChoiceField(source='profile.gender')
    is_admin = serializers.BooleanField(source='profile.is_admin')
    is_company = serializers.BooleanField(source='profile.is_company')
    date_of_birth = serializers.DateTimeField(source='profile.date_of_birth')
    # profile = serializers.PrimaryKeyRelatedField(read_only=False)


    class Meta:
        model = User
        fields = (
            "id",
            "is_active",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_admin",
            "is_company",
            "date_of_birth",
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("is_active", "first_name", "last_name")


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    workstations = serializers.StringRelatedField(many=True)
    work_city = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = (
            "id",
            "is_admin",
            
            "modification_time",
            "is_removed",
            "user",
        )
        extra_kwargs = {
            "workstations": {"required": False},
            "user": {"required": False, "read_only": True},
        }


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "gender",
            "is_company",
            "date_of_birth",
        )





