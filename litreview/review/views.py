from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from review.forms import TicketForm, ReviewForm
from review.models import Ticket, Review

from . import forms
from . import models


@login_required
def home(request):
    return render(request, 'review/home.html')


@login_required
def ticket_create(request):
    """Ticket form"""
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, 'Votre ticket à été créé')
            return redirect('home')
    context = {
        'ticket_form': ticket_form
    }
    return render(request, 'review/create_ticket.html', context=context)


@login_required
def ticket_details(request, ticket_id):
    """Ticket details"""
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'review/ticket_details.html', {'ticket': ticket})


@login_required
def ticket_update(request, ticket_id):
    """Update a ticket"""
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        update_form = TicketForm(request.POST, request.FILES, instance=ticket)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Votre billet à été mis à jour')
            return redirect('ticket_details', ticket_id)
    else:
        update_form = TicketForm(instance=ticket)
    context = {
        'update_form': update_form,
        'ticket': ticket
    }
    return render(request, 'review/ticket_update.html', context=context)


@login_required
def ticket_delete(request, ticket_id):
    """Remove a ticket"""
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        messages.success(request, f'Votre billet {ticket.title} à été supprimé')
        return redirect('home')
    context = {
        'ticket': ticket
    }
    return render(request, 'review/ticket_delete.html', context=context)


@login_required
def review_create(request):
    """Create a review"""
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review_form.save()
            messages.success(request, 'Votre commentaire à été créé')
            return redirect('home')
    context = {
        'review_form': review_form
    }
    return render(request, 'review/review_create.html', context=context)


@login_required
def review_details(request, review_id):
    """Details of a review"""
    review = get_object_or_404(models.Review, id=review_id)
    return render(request, 'review/review_details.html', {'review': review})


@login_required
def review_update(request, review_id, ticket_id):
    """Update a review"""
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        update_form = ReviewForm(request.POST, request.FILES, instance=review)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Commentaire modifié')
            return redirect('home')
    else:
        update_form = ReviewForm(instance=review)
    context = {
        'update_form': update_form,
        'review': review
    }
    return render(request, 'review/review_update.html', context=context)


@login_required
def review_delete(request, review_id):
    """Remove a review"""
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        review.delete()
        messages.success(request, f'Votre commentaire {review.id} à été supprimé')
        return redirect('home')
    context = {
        'review': review,
    }
    return render(request, 'review/review_delete.html', context=context)