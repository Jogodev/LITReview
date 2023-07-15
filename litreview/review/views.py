from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
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
