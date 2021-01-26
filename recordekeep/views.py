from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from .models import Customers
from .filters import CustomersFilter
from .form import CustomersForm
from .models import Messege
import datetime


# Create your views here.
def home(request):
    if request.method=='POST':

        pass
    form = CustomersForm()


    Customerss = Customers.objects.all()
    myFilter=CustomersFilter(request.GET, queryset=Customerss)
    Customerss= myFilter.qs
    mydate=datetime.datetime.now()


    context={'Customerss':Customerss,'form':form,'myFilter':myFilter,'mydate':mydate}




    return render(request,'Home.html',context)
def messege(request):
    if request.method=="POST":

        subject=request.POST['subject']
        messege=request.POST['messege']
        soth=Messege(subject=subject,messege=messege)
        soth.save()
        Emails = Customers.objects.all()
        for hotlemail in Emails:
            hotmail = hotlemail.email
            send_mail(subject,
                      messege,
                      'pradipchapagain123@gmail.com',
                      [hotmail])

















    return render(request, 'Messege.html',)