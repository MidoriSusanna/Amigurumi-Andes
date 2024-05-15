from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FAQ
from .forms import FAQForm


def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'faqs/faq_list.html', {'faqs': faqs})


@login_required
def create_faq(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = FAQForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'New FAQ created successfully.')
                return redirect('faq_list')
        else:
            form = FAQForm()
        return render(request, 'faqs/create_faq.html', {'form': form})
    else:
        messages.error(request, 'You are not authorized to create FAQs.')
        return redirect('faq_list')


@login_required
def edit_faq(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.user.is_superuser:
        if request.method == "POST":
            form = FAQForm(request.POST, instance=faq)
            if form.is_valid():
                form.save()
                messages.success(request, 'FAQ updated successfully.')
                return redirect('faq_list')
        else:
            form = FAQForm(instance=faq)
        return render(request, 'faqs/edit_faq.html', {'form': form})
    else:
        messages.error(request, 'You are not authorized to edit FAQs.')
        return redirect('faq_list')


@login_required
def delete_faq(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.user.is_superuser:
        if request.method == "POST":
            faq.delete()
            messages.success(request, 'FAQ deleted successfully.')
            return redirect('faq_list')
        return render(request, 'faqs/delete_faq.html', {'faq': faq})
    else:
        messages.error(request, 'You are not authorized to delete FAQs.')
        return redirect('faq_list')