from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'count_views', 'is_publication')
    list_filter = ('title', 'created_at', 'is_publication')
    search_fields = ('title',)
