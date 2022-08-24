from django.urls import path

from .views import UserCreateView, UserDeleteView, UserListView

urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('list/', UserListView.as_view()),
    path('delete/<int:pk>/', UserDeleteView.as_view()),
]