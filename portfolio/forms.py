from django import forms

class ContactMeForm(forms.Form):
    email = forms.CharField(max_length = 20)
    subject = forms.CharField()
    message = forms.CharField()