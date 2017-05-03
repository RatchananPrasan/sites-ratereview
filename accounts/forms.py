from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, ModelForm, ImageField, EmailField, EmailInput, TextInput, Textarea
from .models import User, Message, Reply

class RegisterForm(UserCreationForm):
    email = EmailField(label='Email Address',required=True)
    
    class Meta:
        model = User
        fields = ['username', 'password1' , 'password2', 'email']
        
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control','autofocus':True})
        self.fields['password1'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password2'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        
        
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            
        return user
    
    
class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'description']
        labels = {
            'description' : 'About Me',
        }
        widgets = {
            'first_name': TextInput(attrs={'autofocus':True,
                                           'class':'form-control'}),
            
            'last_name': TextInput(attrs={'class':'form-control'}),
            
            'email': EmailInput(attrs={'required':True,
                                       'class':'form-control'}),
            
            'description': Textarea(attrs={'rows': '6',
                                           'class':'text-input'}),
        }
        
        
class ImageUploadForm(Form):
    image = ImageField(label='Upload Image',required=True)

    
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['post']
        widgets = {
            'post': Textarea(attrs={'rows': '6',
                                    'placeholder': 'Write Something.....'})
        }
        
        
class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['reply']
        widgets = {
            'reply': Textarea(attrs={'rows': '4',
                                    'placeholder': 'Write Something.....'})
        }