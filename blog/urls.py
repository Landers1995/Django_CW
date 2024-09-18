from django.urls import path, include
# from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("blog_detail/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
 ]
