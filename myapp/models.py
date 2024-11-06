from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    USER_TYPES = (
        ('Buyer', 'Buyer'),
        ('Seller', 'Seller'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return self.username

    @classmethod
    def get_input_data(cls, data):
        """
        Returns a User instance from the provided input dictionary.
        Example input: {'username': 'johndoe', 'user_type': 'Buyer', 'password': 'mypassword'}
        """
        return cls.objects.create(**data)

# Artist model
class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # References user_id by default
    artist_name = models.CharField(max_length=100)
    artist_image = models.ImageField(upload_to='artist_images/')
    description = models.TextField()

    def __str__(self):
        return self.artist_name

    @classmethod
    def get_input_data(cls, data):
        """
        Returns an Artist instance from the provided input dictionary.
        Example input: {'user': user_instance, 'artist_name': 'Picasso', 'artist_image': 'image_path', 'description': 'Great artist'}
        """
        return cls.objects.create(**data)

# Artwork model
class Artwork(models.Model):
    artwork_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # References user_id by default
    art_title = models.CharField(max_length=150)
    art_image = models.ImageField(upload_to='art_images/')
    art_description = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    art_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.art_title

    @classmethod
    def get_input_data(cls, data):
        """
        Returns an Artwork instance from the provided input dictionary.
        Example input: {'user': user_instance, 'art_title': 'Mona Lisa', 'art_image': 'image_path', 'art_description': 'Famous painting', 'artist': artist_instance, 'art_price': 100000}
        """
        return cls.objects.create(**data)

# Cart model
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # References user_id by default
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Cart {self.cart_id} for user {self.user.username}'

    @classmethod
    def get_input_data(cls, data):
        """
        Returns a Cart instance from the provided input dictionary.
        Example input: {'user': user_instance, 'artist': artist_instance, 'quantity': 2}
        """
        return cls.objects.create(**data)

# Order model
class Order(models.Model):
    STATUS_CHOICES = (
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )
    order_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # References user_id by default
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirmed')
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'Order {self.order_id} by user {self.user.username}'

    @classmethod
    def get_input_data(cls, data):
        """
        Returns an Order instance from the provided input dictionary.
        Example input: {'cart': cart_instance, 'user': user_instance, 'total_price': 200, 'status': 'confirmed', 'quantity': 1}
        """
        return cls.objects.create(**data)
