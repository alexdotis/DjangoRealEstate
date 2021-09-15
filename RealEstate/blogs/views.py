from django.shortcuts import render
from .models import Blog
from django.views import generic
from .serializers import BlogSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 10
    template_name = 'Blogs/listblogs.html'


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'Blogs/blogdetail.html'


class BlogApiView(generics.ListAPIView):
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]
    model = Blog
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
