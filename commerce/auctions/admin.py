from django.contrib import admin

from .models import AuctionListing, Bid, Comment, Category

# Register your models here.
class AuctionListingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "category", "creation_date", "start_bid", "is_active")

class BidAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "listing", "amount")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "listing", "comment")


admin.site.register(Category)
admin.site.register(AuctionListing, AuctionListingAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)