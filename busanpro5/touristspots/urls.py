from django.urls import path, include

from touristspots import views

urlpatterns = [
    path('touristspotslist/', views.TouristSpotsList.as_view()),
    path('touristspot/<int:pk>/', views.TouristSpotDetail.as_view()),
    path('favoritespotslist/', views.MyFavoriteSpotsList.as_view()),
    path('favoritespot/<int:pk>/', views.MyFavoriteSpotsDetail.as_view()),
    path('recommendspots/', views.RecommendList.as_view()),
]