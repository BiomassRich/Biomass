from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .models import *

@login_required(login_url="/accounts/login/")
def addProducts(request):
    productsLog = productsMod.objects.all().order_by('entry_date')
    if request.method == 'POST':
        form = forms.addProductsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.addProductsForm()
    return render(request,'products/addproducts.html',{'form':form,'productsLog':productsLog})

@login_required(login_url="/accounts/login/")
def viewProducts(request):
    productsLog = productsMod.objects.all().order_by('entry_date')
    return render(request,'products/viewproducts.html',{'productsLog':productsLog})
