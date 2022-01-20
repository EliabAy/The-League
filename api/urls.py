from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('player-list/', views.playerList, name='player-list'),
    path('player-detail/<str:pk>/', views.playerDetail, name='player-detail'),
    path('player-create/', views.playerCreate, name='player-create'),
    path('player-update/<str:pk>/', views.playerUpdate, name='player-update'),
    path('player-delete/<str:pk>/', views.playerDelete, name='player-delete'),
]