from django.urls import path

from .views import BadgesCreateView, BadgesListView, BadgesUpdateView, BadgesDeleteView, CategoriesCreateView, CategoriesListView, CategoriesUpdateView, CategoriesDeleteView

urlpatterns = [
    path('badges/create/', BadgesCreateView.as_view()),
    path('badges/list/', BadgesListView.as_view()),
    path('badges/update/<int:pk>/', BadgesUpdateView.as_view()),
    path('badges/delete/<int:pk>/', BadgesDeleteView.as_view()),
    path('categories/create/', CategoriesCreateView.as_view()),
    path('categories/list/', CategoriesListView.as_view()),
    path('categories/update/<int:pk>/', CategoriesUpdateView.as_view()),
    path('categories/delete/<int:pk>/', CategoriesDeleteView.as_view()),
]