from django.http import HttpResponse

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from users.models import Profile, User
from users.serializers import UserCreateSerializer, ProfileSerializer, UserSerializer, UserPasswordUpdateSerializer
from users.filters import UserFilters
from users.pagination import PostLimitOffsetPagination



class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
        serializer.save()


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserPasswordUpdateView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPasswordUpdateSerializer
    permission_classes = [AllowAny]


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


# class ProfileCreateViews(CreateAPIView):
# RetrieveAPIView, RetrieveUpdateAPIView, ListAPIView, 
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     pagination_class = PostLimitOffsetPagination
#     permission_classes = [AllowAny]
#     filterset_class = UserFilters
#     ordering_fields = [
#         "user__username",
#         "user__email",
#     ]
#     ordering = ["user__username", "user__email"]
#     search_fields = ["user__username", "user__email"]

