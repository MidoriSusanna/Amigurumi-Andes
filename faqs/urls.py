from django.urls import path
from . import views

urlpatterns = [
    path('faqs/', views.faq_list, name='faq_list'),
    path('faqs/edit/<int:pk>/', views.edit_faq, name='edit_faq'),
    path('faqs/delete/<int:pk>/', views.delete_faq, name='delete_faq'),
]

