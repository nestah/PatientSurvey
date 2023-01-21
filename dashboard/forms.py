from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            
            'email',
            'password1',
            'password2'
        )


class LoginForm(forms.Form):
    msisdn = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control ',
                'placeholder': 'Phone number'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

class DataForm(forms.ModelForm):

    class Meta : 
          fields = ['name','description','active_till','isActive','number_of_questions', 'target_app']   
          model = QuestionnaireApi  

  