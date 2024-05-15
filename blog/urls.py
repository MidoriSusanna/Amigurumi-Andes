from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='blog'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('new/', PostCreate.as_view(), name='post_form'),
    path('edit/<slug:slug>/', PostUpdate.as_view(), name='post_edit'),
    path('delete/<slug:slug>/', PostDelete.as_view(), name='post_delete'),
]

