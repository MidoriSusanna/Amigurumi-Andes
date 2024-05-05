from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='blog'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('edit/<int:pk>/', PostUpdate.as_view(), name='post_edit'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post_delete'),
    path('approve/<int:pk>/', approve_post, name='post_approve'),
]