from django.shortcuts import render
from .models import FAQ

def faq_list(request):
    faqs = FAQ.objects.all()  # Retrieve all FAQ entries from the database
    return render(request, 'faqs/faq_list.html', {'faqs': faqs})