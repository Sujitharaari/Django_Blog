from django import forms
from . models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 

class DateInput(forms.DateInput):
    input_type='date'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'post_date':DateInput()
        }
labels = {
    'Title': 'Item Name :',
    'Date': 'Date of Order:',
    'Image':'Image :',
    'Content' : 'Content :'
}
class CustomFormUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2','first_name','last_name')