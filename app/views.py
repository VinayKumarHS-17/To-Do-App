from django.shortcuts import render,redirect
from .models import Task,TaskRestore
from .forms import contactForm

# Create your views here.

def home(request):
    read=Task.objects.all()
    b={'read':read}
    return render(request,'home.html',b)


def create(request):
    if request.method == 'POST':
        title=request.POST['title']
        desc=request.POST['desc']
        Task.objects.create(title=title,desc=desc)
        #a=Task.objects.all().delete()
        
    return render(request,'create.html')    


def dele(request,id):
    b=Task.objects.get(id=id)
    c=TaskRestore.objects.create(title=b.title,desc=b.desc)
    # print(b.title,b.desc)
    b.delete()
    c.save()
    return redirect ('home')


def history(request):
    b=TaskRestore.objects.all()
    # per=TaskRestore.objects.all().delete()
    d={'hist':b}
    return render(request,'history.html',d)


def upd(request,id):
    s=Task.objects.get(id=id)
    if request.method=='POST':
        s.title=request.POST['title']
        s.desc=request.POST['desc']
        #Task.objects.create(title=s.title, desc=s.desc)
        s.save()
        return redirect('home')
    d={'updating':s}
    return render(request,'create.html',d)


def about(request):
    return render(request,'about.html')


def restore(request,id):
    b=TaskRestore.objects.get(id=id)
    a=Task.objects.create(title=b.title,desc=b.desc)
    b.delete()
    a.save()
    return redirect('history')


def dele_restore(request,id):
    b=TaskRestore.objects.get(id=id)
    b.delete()
    return redirect('history')


def restore_all(request):
    res=TaskRestore.objects.all()
    for i in res:
        title=i.title
        desc=i.desc
        a=Task.objects.create(title=title,desc=desc)
        a.save()
    res.delete()
    return redirect('history')


def dele_all(request):
    b=TaskRestore.objects.all()
    b.delete()
    return redirect('history')


def contact(request):
    a=contactForm
    b={'data':a}
    return render(request,'contact.html',b)
