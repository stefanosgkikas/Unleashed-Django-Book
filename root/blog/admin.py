from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    date_hierarchy = 'pub_date'
    list_filter = ('pub_date', 'startups')
    search_fields = ('title', 'text')
    prepopulated_fields = {"slug": ("title",)}
