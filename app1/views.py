from django.shortcuts import render,redirect
from app1.models import student
# Create your views here.
from app1.form import S_form

def detail(r):
    data=student.objects.all()

    return render(r,'home.html',{'data':data})


def Stu_F(r):
    form=S_form()
    if r.method=="POST":
        form=S_form(r.POST)
        if form.is_valid():
            form.save()
        return redirect("table")
    return render(r,'new.html',{'form':form})


def S_U(r,id):
    data=student.objects.get(id=id)
    if r.method=="POST":
        form=S_form(r.POST,instance=data)
        if form.is_valid():
            form.save()

        return redirect("table")
    else:
        form=S_form(instance=data)
    return render(r,'new.html',{'form':form})
        

def S_D(r,id):
    data=student.objects.get(id=id)
    data.delete()
    return redirect('table')


# def Main(r):
#     return render(r,'index.html')

# def Count(r):
#     data=student.objects.all()
#     c=len(data)
#     return render(r,'Count.html',{'c':c})
