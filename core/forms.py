from django import forms

from core.models import Contacts


class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contacts
        fields = '__all__'
