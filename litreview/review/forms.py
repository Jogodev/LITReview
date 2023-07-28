from django import forms
from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    """Ticket form"""

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    """Review form"""

    class Meta:
        model = Review
        fields = ['headline', 'body', 'rating']
