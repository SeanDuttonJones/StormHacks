# forms.py 

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
  


class PostForm(forms.ModelForm): 
    """
    Logging into Website Form
    """
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=100)
    
    date_posted = forms.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img = forms.ImageField(upload_to='images/')

    def __init__(self,args,**kwargs):
        super().__init__(args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout (
            Fieldset(
                " ",
                "title",
                "content",
                "date_posted",
                "author",
                "img"
            ),
            ButtonHolder(
                Submit('submit','Login Data',css_class='button white'),

            ),

        )