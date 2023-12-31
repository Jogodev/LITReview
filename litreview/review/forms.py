from django import forms
from .models import Ticket, Review
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineRadios
from crispy_forms.layout import Field, Layout, Div


class TicketForm(forms.ModelForm):
    """Ticket form"""

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titre',
            'description': 'Description',
        }


class ReviewForm(forms.ModelForm):
    """Review form"""
    rating = forms.ChoiceField(
        choices=((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")),
        widget=forms.RadioSelect(),
        label="Note"
    )

    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        widgets = {'rating': forms.RadioSelect()}
        labels = {
            'headline': 'Titre',
            'body': 'Commentaire',
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        self.helper.layout = Layout(
            Div(InlineRadios('rating', css_class='custom-control-label')),
        )
