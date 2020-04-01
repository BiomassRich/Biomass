from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def homepage(request):
    return render(request,'homepage.html')

@login_required(login_url="/accounts/login/")
def error_404(request,exception):
        data = {}
        return render(request,'error_404.html', data)

@login_required(login_url="/accounts/login/")
def error_500(request):
        data = {}
        return render(request,'error_500.html', data)
