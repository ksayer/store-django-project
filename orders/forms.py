from django_countries.fields import CountryField
from django import forms

from orders.models import Order


class PaymentForm(forms.Form):
    country = CountryField().formfield()
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': "form-control"}))
    address1 = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'class': "form-control"}))
    address2 = forms.CharField(max_length=250, required=False, widget=forms.TextInput(
        attrs={'class': "form-control"}))
    phone = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'class': "form-control"}))
    city = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'class': "form-control"}))

    class Meta:
        model = Order
        fields = ('country', 'name', 'address1', 'address2', 'city', 'phone')
