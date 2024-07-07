from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)
        # Only superusers can modify the 'status' field
        if user and not user.is_superuser:
            self.fields.pop('status', None)  # Hide 'status' from non-superusers

    class Meta:
        model = Post
        fields = [
            'title', 'slug', 'featured_image', 'excerpt', 'content', 'status'
        ]
        widgets = {
            'content': SummernoteWidget(),  # Enables rich text editing
        }
