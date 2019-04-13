from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms


class RestaurantForm(forms.Form):
    name = forms.CharField(label='Name')
    address = forms.CharField(label='Address', required=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'POST'