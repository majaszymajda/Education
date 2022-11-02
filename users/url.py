from django.urls import path

from .views import UserCreateView, UserDeleteView, UserListView, UserPasswordUpdateView

urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('list/', UserListView.as_view()),
    path('update/<int:pk>/', UserListView.as_view()),
    path('update-password/<int:pk>/', UserPasswordUpdateView.as_view()),
    path('delete/<int:pk>/', UserDeleteView.as_view()),
]