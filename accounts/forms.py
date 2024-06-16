from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    class Meta:
        model=User 
        fields=['username','email','password1','password2']
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email=self.cleaned_data['email']
        user.username=self.cleaned_data['username']
        user.last_name=self.cleaned_data['last_name']
        user.first_name=self.cleaned_data['first_name']
    
        if commit:
            user.save()
        return user