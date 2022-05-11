
from django import forms

from apps.orders.models import Order

from apps.products.models import Product


class CheckoutForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name_shop'].required = True
        self.fields['city'].required = True

    class Meta:
        model = Order
        fields = (
            'name_shop',
            'city',
            'mobile',
            'delivery_method',
            'delivery_district_address',
            'delivery_region_address',
            'post_office',
            'numbers'
        )


class QuickCheckoutForm(forms.Form):

    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=forms.HiddenInput)

    mobile = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your mobile'
        })
    )
