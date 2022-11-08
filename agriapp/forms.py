from django import forms
from .models import ContactDetails

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields = ['mail', 'phone', 'message', 'name']
