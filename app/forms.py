from .models import Contact
from django import forms


class contactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','phno','email','suggestion'] 
        