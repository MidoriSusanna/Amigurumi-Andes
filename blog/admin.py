from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'author')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish_posts', 'draft_posts']

    def publish_posts(self, request, queryset):
        queryset.update(status=1)
    publish_posts.short_description = "Mark selected posts as Published"

    def draft_posts(self, request, queryset):
        queryset.update(status=0)
    draft_posts.short_description = "Mark selected posts as Draft"

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)

