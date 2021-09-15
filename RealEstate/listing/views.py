from django.views import generic
from rest_framework.response import Response
from .models import Listing, ListingImages, ExtraFeature, ListingReview
from django.shortcuts import render

from django_filters.views import FilterView
from .filters import ListingFilter, HomepageFilterForm

from .serializers import ListingCreateReviewSerializer,ListingReviewSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from authentication.models import Agent
from rest_framework.renderers import JSONRenderer


class HomepageView(FilterView):
    template_name = 'HomePage/homepage.html'
    filterset_class = HomepageFilterForm
    model = Listing

    def get_queryset(self):
        return Listing.objects.filter(active=True).order_by('-created_at')[:5]


class ListingListView(FilterView):
    template_name = 'listing/index.html'
    filterset_class = ListingFilter
    model = Listing
    paginate_by = 10

    def get_queryset(self):
        return Listing.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_copy = self.request.GET.copy()

        if get_copy.get('sort_by'):
            get_copy.pop('sort_by')

        if get_copy.get('page'):
            get_copy.pop('page')
        context['params'] = get_copy
        return context


class ListingDetailView(generic.DetailView):
    template_name = 'Detailview/index.html'
    model = Listing

    def get_context_data(self, **kwargs):

        context = super(ListingDetailView, self).get_context_data(**kwargs)

        context['images'] = ListingImages.objects.filter(
            listing=self.get_object())
        context['features'] = ExtraFeature.objects.filter(
            listing=self.get_object())
        context['reviews'] = ListingReview.objects.filter(
            listing=self.get_object())
        try:
            context['agent'] = Listing.objects.get(title=self.get_object()).agent
        except Agent.DoesNotExist:
            context['agent'] = ''

        return context


class ApiListingReviewList(ListAPIView):
    serializer_class = ListingReviewSerializer
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        qs = ListingReview.objects.filter(listing__slug=self.kwargs['slug'])
        return qs

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        load = serializer.data

        response_list = {'count': len(serializer.data), 'results': load}
        return Response(response_list)


class ApiCreateListingReview(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListingCreateReviewSerializer
    model = ListingReview

    def perform_create(self, serializer):
        listing = Listing.objects.get(slug=self.kwargs['slug'])
        serializer.save(user=self.request.user, listing=listing)




def handler404(request, *args, **kwargs):
    
    response = render(request,'pages/404.html')
    response.status_code = 404
    return response



def handler500(request, *args, **kwargs):
    
    response = render(request,'pages/404.html')
    response.status_code = 500
    return response