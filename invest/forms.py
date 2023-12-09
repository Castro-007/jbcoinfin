from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Deposit, Profile


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        
        return user
    

class EditUserForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
 

class DepositForm(forms.ModelForm):

    class Meta:
        model = Deposit
        fields = ('deposit', 'plan', 'gateway')


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('country', 'phone_number', 'state', 'zip_code', 'city', 'address')