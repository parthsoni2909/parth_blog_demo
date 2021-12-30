from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'last name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Enter email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Enter Unique username'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Enter Password','type':'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Confirm Password','type':'password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image','city','skill']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'last name'}))

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']

class PasswordChangeForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Enter Old Password','type':'password'}))
    new_password = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Enter New Password','type':'password'}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Confirm Password','type':'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'confirm_password']