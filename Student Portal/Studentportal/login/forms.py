from django import forms
from .models import login





class login_identifier(forms.ModelForm):
    user_name_principle=forms.CharField(widget=forms.TextInput(),required=True)
    password_principle=forms.CharField(widget=forms.PasswordInput,require=True)
    
    
   
    
    class Meta():
        model = login
        fields = ['user_name_principle','pasword_principle']
   

  