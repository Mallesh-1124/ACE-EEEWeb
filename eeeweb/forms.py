from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'roll_number', 'message']

    def clean_roll_number(self):
        roll = self.cleaned_data['roll_number']
        if len(roll) != 10:
            raise forms.ValidationError("Roll number must be exactly 10 characters.")
        return roll
