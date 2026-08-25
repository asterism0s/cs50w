from django.forms import ModelForm
from .models import AuctionListing

class ListingForm(ModelForm):
    class Meta:
        model = AuctionListing
        fields= [ "image", "title", "category", "description", "start_bid"]