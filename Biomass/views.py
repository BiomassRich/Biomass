from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from datetime import datetime


@login_required(login_url="/accounts/login/")
def homepage(request):
    return render(request,'homepage.html')

@login_required(login_url="/accounts/login/")
def permit(request):
    if request.method == 'POST':
        f = request.FILES['sentFile']
        fs = FileSystemStorage()
        cDate = datetime.now().strftime("%d%m%Y%H%M%S")
        fName = f.name.replace(".pdf","") + cDate +".pdf"
        filename = fs.save(fName, f)
        #uploaded_file_url = fs.url(filename)
        #print(uploaded_file_url)
    else:
        pass
    return render(request,'permit.html')


def offlinePage(request):
    return render(request,'offline.html')

@login_required(login_url="/accounts/login/")
def error_404(request,exception):
        data = {}
        return render(request,'error_404.html', data)

@login_required(login_url="/accounts/login/")
def error_500(request):
        data = {}
        return render(request,'error_500.html', data)
