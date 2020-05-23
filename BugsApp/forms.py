from django import forms
from . models import Ticket
from .models import Customeuser
class Ticketform(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=('title','Description')

class EditForm(forms.ModelForm):
    assigned_to=forms.ModelChoiceField(queryset=Customeuser.objects.all(), required=False)
    completed_by=forms.ModelChoiceField(queryset=Customeuser.objects.all(),required=False)
    class Meta:
        model=Ticket
        fields=('title','Description','filed_by','assigned_to','completed_by')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customeuser
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'Age', ]