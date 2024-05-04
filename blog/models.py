from django.db import models
from django.contrib.auth.models import User


# Set 0 or 1 whether the post is draft or published
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """ Create Django POST model from the database scheme """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = models.ImageField(upload_to='images/', default='images/placeholder.png')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title