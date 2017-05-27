from django.forms import Form, ModelForm, TextInput, Textarea, NumberInput, HiddenInput, ImageField, Select, CharField, BaseFormSet, ValidationError, HiddenInput
from .models import Recipe, Category, Rating

class RecipeInitialForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'calories', 'prep_time', 'serving']
        labels = {
            'title' : 'Recipe Name',
            'description' : 'About Recipe',
            'calories': 'Calories(kcal)',
            'prep_time' : 'Preparation Time(in minutes)',
            'serving' : 'Serving Size',
        }
        widgets = {
            'title' : TextInput(attrs={'autofocus':True,
                                       'class':'form-control'}),
            
            'description': Textarea(attrs={'class':'form-control text-input',
                                           'rows': '4'}),
                        
            'calories': NumberInput(attrs={'class':'form-control'}),
            
            'prep_time': NumberInput(attrs={'class':'form-control'}),
            
            'serving': NumberInput(attrs={'class':'form-control'}),
        }
        
        
class ImageUploadForm(Form):
    image = ImageField(required=False)
    
    def __init__(self, *args, **kwargs):
        super(ImageUploadForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class' : 'file-input'})
    

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': Select(attrs={'class':'form-control'})
        }
        
        
class TextForm(Form):
    text = CharField()
    
    def __init__(self, *args, **kwargs):
        super(TextForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class' : 'form-control'})
        
        
class BaseTextFormSet(BaseFormSet):
    
    def clean(self):
        if any(self.errors):
            return
        
        texts = []
        for form in self.forms:
            if form.cleaned_data:
                texts.append(form.cleaned_data['text'])
           
        if not texts:
            raise ValidationError("Need at least one field")
            
            
class BaseCategoryFormSet(BaseFormSet):
    
    def clean(self):
        if any(self.errors):
            return
        
        categories = []
        for form in self.forms:
            if form.cleaned_data:
                categories.append(form.cleaned_data['title'])
           
        if not categories:
            raise ValidationError("Need at least one category")
            
            
class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['rate', 'description']
        widgets = {
            'rate': HiddenInput(),
            'description': Textarea(attrs={'rows':'4',
                                           'cols':'50',
                                           'placeholder':'Optional Description',
                                           'class':'form-control',
                                           'style':'width:auto;margin-bottom:15px;'})
        }