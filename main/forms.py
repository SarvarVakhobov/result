from .models import *

class Form(forms.ModelForm):
    
    class Meta:
        model = Result
        fields = ("number",)
