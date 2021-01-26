import django_filters
from django_filters import DateFilter
from  .models import *


class CustomersFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name="insertdate",lookup_expr='gte')
    end_date = DateFilter(field_name="insertdate", lookup_expr='lte')
    class Meta:
        model= Customers
        fields= '__all__'
        exclude=['dob','permanentadd','insertdate']
