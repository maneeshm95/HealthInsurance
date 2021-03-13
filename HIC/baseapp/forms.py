from django import forms
from .models import Contact



class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    mobile = forms.IntegerField()

class ContactModelForm(forms.ModelForm):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={
        'class':'form-control bg-light'
    }
    ))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'class':'form-control bg-light'}
    ))
    mobile = forms.CharField(label="Mobile",  widget=forms.TextInput(attrs={
        'class':'form-control bg-light'
    }
    ))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={
        'class':'form-control bg-light'
    }
    ))


    class Meta:
        model = Contact
        fields = '__all__'

