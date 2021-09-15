from django.urls import path
from .views import  BlogListView, BlogDetailView,BlogApiView


urlpatterns = [
    path('',BlogListView.as_view(),name='blog_list'),
    path('<slug>',BlogDetailView.as_view(),name='blog_detail'),
    path('api/',BlogApiView.as_view())

]
