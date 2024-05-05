from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='blog'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('new/<slug:slug>/', PostCreate.as_view(), name='post_form'),
    path('edit/<int:pk>/', PostUpdate.as_view(), name='post_edit'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post_delete'),
]