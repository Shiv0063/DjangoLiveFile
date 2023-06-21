from django.shortcuts import render,redirect
from main.models import file
# Create your views here.
def home(request):
    dt=file.objects.all()
    data={
        'data':dt
    }
    return render(request,'index.html',data)

def cf(request):
    dt=file.objects.all()
    data={
        'data':dt
    }
    if request.method=='POST':
        files = request.FILES['file']
        print(files)
        data =file.objects.create(file=files)
        data.save()
        return redirect('/cf')
    return render(request,'file.html',data)

def delete(request,id):
    dt=file.objects.get(id=id)
    dt.delete()
    return redirect('/cf')