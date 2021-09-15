from rest_framework import serializers
from .models import ListingReview


class ListingReviewSerializer(serializers.ModelSerializer):
    listing = serializers.CharField(default='listing')
    user = serializers.CharField(default='user')

    class Meta:
        model = ListingReview
        fields = '__all__'


class ListingCreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingReview
        fields = ('comment', 'review')
