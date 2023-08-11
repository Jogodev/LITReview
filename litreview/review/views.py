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
    """Create a ticket and the review"""
    review_form = ReviewForm(request.POST)
    ticket_form = TicketForm(request.POST, request.FILES)
    if request.method == 'POST':
        if review_form.is_valid() and ticket_form.is_valid():
            new_ticket = Ticket.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                image=request.FILES['image'],
                user=request.user
            )
            new_ticket.save()
            new_review = Review.objects.create(
                ticket=new_ticket,
                rating=request.POST['rating'],
                headline=request.POST['headline'],
                body=request.POST['body'],
                user=request.user,
            )
            new_review.save()
            messages.success(request, 'Ticket et commentaire créés')
            return redirect('home')
        else:
            review_form = ReviewForm()
            ticket_form = TicketForm()
    context = {
        'review_form': review_form,
        'ticket_form': ticket_form,
    }
    return render(request, 'review/review_create.html', context)


@login_required
def review_answer(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            Review.objects.create(
                ticket=ticket,
                rating=request.POST['rating'],
                headline=request.POST['headline'],
                body=request.POST['body'],
                user=request.user,
            )
        messages.success(request, 'Commentaire créé')
        return redirect('home')
    else:
        review_form = ReviewForm()
    context = {
        'review_form': review_form,
        'ticket': ticket,
    }
    return render(request, 'review/review_answer.html', context)


@login_required
def review_details(request, review_id):
    """Details of a review"""
    review = get_object_or_404(models.Review, id=review_id)
    return render(request, 'review/review_details.html', {'review': review})


@login_required
def review_update(request, review_id):
    """Update a review"""
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        update_form = ReviewForm(request.POST, request.FILES, instance=review)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Commentaire modifié')
            return redirect('review_details')
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
        messages.success(request, f'Votre commentaire {review.title} à été supprimé')
        return redirect('home')
    context = {
        'review': review,
    }
    return render(request, 'review/review_delete.html', context=context)
