from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListings(models.Model):
    FASHION = "FA"
    ELECTRONICS = "EL"
    FURNITURE = "FU"
    TOYS = "TO"
    SPORTS = "SP"
    BOOKS = "BO"
    ART = "AR"
    VEHICLES = "VE"
    NOT_DEFINED = "ND"

    CATEGORIES_CHOICES = {
        FASHION: "Fashion",
        ELECTRONICS: "Electronics",
        FURNITURE: "Furniture",
        TOYS: "Toys",
        SPORTS: "Sports",
        BOOKS: "Books",
        ART: "Art",
        VEHICLES: "Vehicles",
        NOT_DEFINED: "Not defined"
    }


    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_listings")
    category = models.CharField(max_length=2, choices=CATEGORIES_CHOICES, default=NOT_DEFINED, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    image = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=64)
    start_bid  = models.DecimalField(max_digits=8, decimal_places=2)


    def __str__ (self):
        return f"{self.title} ({self.author})"