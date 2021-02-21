from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Fieldset, ButtonHolder, Submit

class Login(forms.Form):
    """
    Logging into Website Form
    """
    username = forms.CharField(label = 'username' , max_length = 200 , required = True)
    password = forms.CharField(label = 'password' , max_length = 200 , required = True , widget = forms.PasswordInput())

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout (
            Fieldset(
                " ",
                Div("username",
                "password",
                css_id="form-control")
            ),
            ButtonHolder(
                Submit('submit','Login Data',css_class='button white'),

            ),

        )
class Register(forms.Form):
    """
    Registering to Website Form
    """
    CHOICES=[('Business','Business'),('Shopper','Shopper')]

    username = forms.CharField(label = 'username' , max_length = 200 , required = True)
    password = forms.CharField(label = 'password' , max_length = 200 , required = True , widget = forms.PasswordInput())
    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect , required=True)
    first_name = forms.CharField(label = 'first_name' , max_length = 200 , required = False)
    last_name = forms.CharField(label = 'last_name' , max_length = 200 , required = False)
    

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout (
            Fieldset(
                " ",
                "first_name",
                "last_name",
                "username",
                "password",
                "choice",

            ),
            ButtonHolder(
                Submit('submit','Register Data',css_class='button white'),
                
            ),
        )

class Business(forms.Form):
    """
    Registering to Business form
    """
    description = forms.CharField(widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout (
            Fieldset(
                " ",
                "description",
            

            ),
            ButtonHolder(
                Submit('submit','Register Data',css_class='button white'),
                
            ),
        )

class Shopper(forms.Form):
    """
    Registering to Shopper form
    """
    description = forms.CharField(widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout (
            Fieldset(
                " ",
                "description",
                

            ),
            ButtonHolder(
                Submit('submit','Register Data',css_class='button white'),
                
            ),
        )