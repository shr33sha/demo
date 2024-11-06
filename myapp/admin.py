from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Artist, Artwork, Cart, Order

# Register the custom User model
# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ('username', 'user_type', 'email')
#     list_filter = ('user_type',)
#     search_fields = ('username', 'email')
#     ordering = ('username',)

# Register the Artist model
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('artist_name', 'user', 'description')
    search_fields = ('artist_name', 'description')

# Register the Artwork model
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('art_title', 'artist', 'art_price', 'user')
    search_fields = ('art_title', 'artist__artist_name', 'art_price')

# Register the Cart model
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'artist', 'quantity')
    list_filter = ('user', 'artist')
    search_fields = ('user__username', 'artist__artist_name')

# Register the Order model
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'status', 'date', 'quantity')
    list_filter = ('status', 'date')
    search_fields = ('user__username', 'status')

# Register all models
admin.site.register(User)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
