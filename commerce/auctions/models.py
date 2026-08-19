from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category (models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class AuctionListing(models.Model):

    author = models.ForeignKey(User, related_name="created_listings", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="listings", on_delete=models.SET_NULL, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=64)
    start_bid  = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__ (self):
        return f"{self.title} ({self.author})"

class Bid(models.Model):
    author = models.ForeignKey(User, related_name="created_bids", on_delete=models.CASCADE)
    listing = models.ForeignKey(AuctionListing, related_name="bids", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Bid of {self.amount} on {self.listing} by {self.author}"

class Comment(models.Model):
    author= models.ForeignKey(User, related_name="created_comments", on_delete=models.CASCADE)
    listing = models.ForeignKey(AuctionListing, related_name="comments", on_delete= models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"Comment made by {self.author} on {self.listing}"