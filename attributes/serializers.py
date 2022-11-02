
from django.contrib.auth import authenticate, password_validation
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers

from users.models import Profile, User
from attributes.models import Interests, Categories, Badges, ToLernCategories

class InterestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interests
        fields = (
            "name",
            "is_active",
        )


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = (
            "name",
            "is_active",
        )


class BadgesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badges
        fields = (
            "name",
            "is_active",
            "category",
        )


class ToLernCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToLernCategories
        fields = (
            "name",
            "is_active",
        )

