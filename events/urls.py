from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('join/', views.join_event, name='join_event'),
    path('leave/<int:event_id>/', views.leave_event, name='leave_event'),
    path('my_events/', views.my_events, name='my_events'),
]
