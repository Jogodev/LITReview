from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from . import models
from review.models import Ticket, Review
from review.forms import TicketForm


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
