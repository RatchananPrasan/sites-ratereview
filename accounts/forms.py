from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, ModelForm, ImageField, EmailField, EmailInput, TextInput, Textarea
from .models import User, Message, Reply

class RegisterForm(UserCreationForm):
    email = EmailField(label='Email Address',required=True)
    
    class Meta:
        model = User
        fields = ['username', 'password1' , 'password2', 'email']
        widgets = {
            'username': TextInput(attrs={'autofocus':True})
        }
        
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
            'first_name': TextInput(attrs={'autofocus':True}),
            'email': EmailInput(attrs={'required':True}),
            'description': Textarea(attrs={'rows': '6'}),
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