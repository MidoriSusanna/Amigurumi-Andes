from django.urls import path
from . import views

urlpatterns = [
    path('faqs/', views.faq_list, name='faq_list'),
]
