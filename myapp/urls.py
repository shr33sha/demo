# urls.py
from django.urls import path
from . import views
from .views import RegisterUserView, ArtistListView, ArtworkListView, CartView, OrderView, LoginView

urlpatterns = [
    path('create_user/', views.create_user, name='create_user'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('artists/', ArtistListView.as_view(), name='artist-list'),
    path('artworks/', ArtworkListView.as_view(), name='artwork-list'),
    path('cart/', CartView.as_view(), name='cart'),
    path('orders/', OrderView.as_view(), name='order'),
]
