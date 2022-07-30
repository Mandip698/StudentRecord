from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from django.contrib import messages
import os


def index(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        gender=request.POST.get('gender')
        address=request.POST['address']
        phone=request.POST['phone']
        language=','.join(map(str,request.POST.getlist('language')))
        country=request.POST['country']
        image=''
        if request.FILES:
            image=request.FILES['image']
        Student.objects.create(
            name=name,email=email,gender=gender,address=address,phone=phone,language=language,country=country,image=image
        )
        messages.success(request,'Record Added Successfully')
        redirect_back_url=request.META.get('HTTP_REFERER')
        return redirect(redirect_back_url)
    else:
        data={
            'studentsData':Student.objects.order_by('-id')
        }
        return render(request,'index.html',data)

def delete_file(id):
    f_data=Student.objects.get(id=id)
    if f_data.image:
        file_path = os.getcwd() + f_data.image.url
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        else:
            return True
    else:
        return True

# delete file function

def delete(request,id):
    if delete_file(id) and Student.objects.get(id=id).delete():
        messages.success(request,'Record Deleted Successfully')
        redirect_back_url=request.META.get('HTTP_REFERER')
        return redirect(redirect_back_url)
    else:
        redirect_back_url=request.META.get('HTTP_REFERER')
        return redirect(redirect_back_url)


def update(request,id):
    if request.method=="POST":
        sObject=Student.objects.get(id=id)
        sObject.name=request.POST['name']
        sObject.email=request.POST['email']
        sObject.gender=request.POST.get('gender')
        sObject.address=request.POST['address']
        sObject.phone=request.POST['phone']
        sObject.language=','.join(map(str,request.POST.getlist('language')))
        sObject.country=request.POST['country']
        image=''
        if request.FILES:
            delete_file(id)
            image=request.FILES['image']
        sObject.image=image
        sObject.save()
        messages.success(request,'Record Updated Successfully')
        redirect_back_url=request.META.get('HTTP_REFERER')
        return redirect(redirect_back_url)
    else:
        data={
            
            'studentData':Student.objects.get(id=id)
        }
        return render(request,'update.html',data)