from django.urls import path
from .views import (
    ListingListView,
    ListingDetailView,
    ApiListingReviewList,
    ApiCreateListingReview
)


urlpatterns = [
    path('', ListingListView.as_view(), name='listing'),
    path('<slug>', ListingDetailView.as_view(), name='detail'),
    path('api/property/<slug>/review', ApiListingReviewList.as_view()),
    path('api/property/<slug>/review/create',
         ApiCreateListingReview.as_view()),

]
