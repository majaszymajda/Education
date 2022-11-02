from django.http import HttpResponse

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from attributes.models import Interests, Categories, Badges, ToLernCategories
from attributes.serializers import InterestsSerializer, CategoriesSerializer, BadgesSerializer, ToLernCategoriesSerializer



class InterestsCreateView(CreateAPIView):
    queryset = Interests.objects.all()
    serializer_class = InterestsSerializer
    permission_classes = [AllowAny]

class InterestsListView(ListAPIView):
    queryset = Interests.objects.all()
    serializer_class = InterestsSerializer
    permission_classes = [AllowAny]

class InterestsUpdateView(RetrieveUpdateAPIView):
    queryset = Interests.objects.all()
    serializer_class = InterestsSerializer
    permission_classes = [AllowAny]


class InterestsDeleteView(DestroyAPIView):
    queryset = Interests.objects.all()
    serializer_class = InterestsSerializer
    permission_classes = [AllowAny]



class BadgesCreateView(CreateAPIView):
    queryset = Badges.objects.all()
    serializer_class = BadgesSerializer
    permission_classes = [AllowAny]

class BadgesListView(ListAPIView):
    queryset = Badges.objects.all()
    serializer_class = BadgesSerializer
    permission_classes = [AllowAny]

class BadgesUpdateView(RetrieveUpdateAPIView):
    queryset = Badges.objects.all()
    serializer_class = BadgesSerializer
    permission_classes = [AllowAny]


class BadgesDeleteView(DestroyAPIView):
    queryset = Badges.objects.all()
    serializer_class = BadgesSerializer
    permission_classes = [AllowAny]



class CategoriesCreateView(CreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [AllowAny]


class CategoriesListView(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [AllowAny]


class CategoriesUpdateView(RetrieveUpdateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [AllowAny]


class CategoriesDeleteView(DestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [AllowAny]




class ToLernCategoriesCreateView(CreateAPIView):
    queryset = ToLernCategories.objects.all()
    serializer_class = ToLernCategoriesSerializer
    permission_classes = [AllowAny]


class ToLernCategoriesListView(ListAPIView):
    queryset = ToLernCategories.objects.all()
    serializer_class = ToLernCategoriesSerializer
    permission_classes = [AllowAny]


class ToLernCategoriesUpdateView(RetrieveUpdateAPIView):
    queryset = ToLernCategories.objects.all()
    serializer_class = ToLernCategoriesSerializer
    permission_classes = [AllowAny]


class ToLernCategoriesDeleteView(DestroyAPIView):
    queryset = ToLernCategories.objects.all()
    serializer_class = ToLernCategoriesSerializer
    permission_classes = [AllowAny]