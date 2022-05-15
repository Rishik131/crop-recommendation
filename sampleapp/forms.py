from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import snippet
class cropdetails(forms.Form):
    district = forms.CharField()
    village = forms.CharField()
    pH = forms.CharField()
    moisture = forms.CharField()
    nitrogen = forms.CharField()
    phosphorus = forms.CharField()
    zinc = forms.CharField()
    potassium = forms.CharField()
    iron = forms.CharField()
    copper = forms.CharField()

    # def __init__(self,*args,**kwargs):
    #     super.__init__(*args,**kwargs)
    #     self.helper = FormHelper
    #     self.helper.form_method = 'post'
class snippetform(forms.ModelForm):
    class Meta:
            model = snippet
            fields = ('district','village', 'pH', 'moisture','nitrogen','phosphorus','zinc','potassium','iron','copper')

