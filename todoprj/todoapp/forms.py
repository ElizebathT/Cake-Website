from django import forms
from .models import tab
class create_form(forms.ModelForm):
    class Meta:
        model=tab
        fields='__all__'