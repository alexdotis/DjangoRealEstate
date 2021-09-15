from django.contrib import admin
from .models import Listing, ExtraFeature, ListingImages, ListingReview


class ExtraFeatureAdmin(admin.ModelAdmin):
    model = ExtraFeature
    list_display = ['feature', 'get_listing_title', 'choice']
    list_filter = ['choice']
    search_fields = ['feature']

    def get_listing_title(self, obj):
        return obj.listing.title


class ExtraFeatureInLine(admin.TabularInline):
    model = ExtraFeature


class ListingImageInLine(admin.TabularInline):
    model = ListingImages


class ListingAdminInline(admin.ModelAdmin):
    model = Listing
    inlines = [ExtraFeatureInLine, ListingImageInLine]
    list_display = ['title', 'updated_at',
                    'status', 'image', 'created_at', 'slug','agent']
    search_fields = ['title','agent__user__username']
    list_filter = ['status']




class ListingReviewAdmin(admin.ModelAdmin):
    model = ListingReview
    list_display = ['get_listing', 'get_user', 'comment', 'review']
    search_fields = ['user__username', 'listing__title']

    def get_listing(self, obj):
        return obj.listing.title

    def get_user(self, obj):
        return obj.user.username


admin.site.register(Listing, ListingAdminInline)
admin.site.register(ExtraFeature, ExtraFeatureAdmin)
admin.site.register(ListingImages)
admin.site.register(ListingReview, ListingReviewAdmin)
