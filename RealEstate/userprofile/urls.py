from django.urls import path
from .views import (
    AgentProfileUpdateView,
    AgentPropertyCreateView,
    AgentPropertyListView,
    AgentPropertyUpdateView,
    AgentDeleteProperty,
    # users
    UserProfileUpdateView,
    UserAssignedPropertyListView,
    UserPropertyCreateView,
    UserAssignedPropertyDetailView,
    UserPropertyListView,
    UserPropertyUpdateView,
    # api
    SubCategoryApiView,


)

urlpatterns = [
    path('<pk>/', UserProfileUpdateView.as_view(), name='user_profile'),
    path('agent/<pk>/', AgentProfileUpdateView.as_view(), name='agent_profile'),
    path('agent/create/property', AgentPropertyCreateView.as_view(),
         name='agent_create_property'),
    path('agent/detail/user-assinged/properties/<pk>/',
         UserAssignedPropertyDetailView.as_view(), name='user_assigned_property_detail'),
    path('agent/user/assigned/properties',
         UserAssignedPropertyListView.as_view(), name='user_assigned_properties'),
    path('agent/my-properties', AgentPropertyListView.as_view(),
         name='agent_property_list'),
    path('agent/update-property/<pk>', AgentPropertyUpdateView.as_view(),
         name='agent_update_property'),
    path('agent/delete-property/<pk>', AgentDeleteProperty.as_view(),
         name='agent_delete_property'),
    path('user/create/property', UserPropertyCreateView.as_view(),
         name='user_create_property'),
    path('user/my-properties', UserPropertyListView.as_view(),
         name='user_properties'),
    path('user/update-property/<pk>', UserPropertyUpdateView.as_view(),
         name='user_update_property'),

    path('api/subcategory/', SubCategoryApiView.as_view()),


]
