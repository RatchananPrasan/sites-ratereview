from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE, 
                                primary_key = True)
    
    image = models.ImageField(upload_to='media/accounts/profile',
                              default='media/accounts/profile/default.jpg')
    
    
class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'username': TextInput(attrs={'class':'form-control','autofocus':True}),
            'password': PasswordInput(attrs={'class':'form-control'}),
            'email': EmailInput(attrs={'class':'form-control'})
        }