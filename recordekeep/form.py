from django.forms import ModelForm,TextInput
from .models import Customers



class CustomersForm(ModelForm):
    class Meta:
        model=Customers
        fields = '__all__'
        id="myInput"
        onkeyup="myFunction()"




