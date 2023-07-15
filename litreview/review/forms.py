from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    """Ticket form"""
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
