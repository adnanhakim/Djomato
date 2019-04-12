from django import forms


class RestaurantForm(forms.Form):
    name = forms.CharField(label='Name')
    address = forms.CharField(label='Address')