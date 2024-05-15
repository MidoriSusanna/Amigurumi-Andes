from django.contrib import admin
from django.contrib import messages
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'status', 'created_on', 'author')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    def publish_posts(self, request, queryset):
        """Check if the user is a superuser."""
        if request.user.is_superuser:
            queryset.update(status=1)
            messages.success(
                request,
                "Selected posts have been marked as published."
            )
        else:
            messages.error(
                request,
                "You do not have permission to perform this action."
            )
    publish_posts.short_description = "Mark selected posts as Published"

    def draft_posts(self, request, queryset):
        """Check if the user is a superuser."""
        if request.user.is_superuser:
            queryset.update(status=0)
            messages.success(
                request,
                "Selected posts have been marked as draft."
            )
        else:
            messages.error(
                request,
                "You do not have permission to perform this action."
            )
    draft_posts.short_description = "Mark selected posts as Draft"

    def save_model(self, request, obj, form, change):
        """Automatically set the author of the post to the current user."""
        if not obj.pk:  # Check if this is a new object being created
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
