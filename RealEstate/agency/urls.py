from django.urls import path
from .views import AgenyListView,AgencyDetailView

urlpatterns = [
       path('agency-list',AgenyListView.as_view(),name='agency_list'),
       path('agent/<user>/',AgencyDetailView.as_view(),name='agency_profile')

]
