from django.shortcuts import render
from login.models import login_teacher,login_principle
from django.http import *
from django.contrib import messages
from .models import addteacher
from .forms import addsubject_form, addteacher_form

# Create your views here.


def addteacher1(request):
    if request.method == 'POST':
       
        Teacher_Username = request.POST['Teacher_Username']
        Teacher_Password = request.POST['Teacher_Password']
        Teacher_Password2 = request.POST['Teacher_Password2']
     
    
    if Teacher_Password == Teacher_Password2 :
            
            
            if login_teacher.objects.filter(user_name_teacher = Teacher_Username).exists():
                messages.info(request, 'username exists')
                return render(request, 'createteacher.html')
            else:
                form=addteacher_form(request.POST)
                print(form.errors)

                
                if form.is_valid():

                    instance = form.save(commit=False)
                    subject = form.cleaned_data.get("Teacher_Subject")
                    instance.Teacher_Subject.set(subject)
                   
                   
                    
                    instance.save()
            
                    return redirect('/')

                user_teacher = login_teacher.objects.create(user_name_teacher=Teacher_Username, password_teacher=Teacher_Password)

               
                user_teacher.save()
                return render(request, 'createteacher.html')
    else:
         return render(request, 'principlehome.html')



    
    if request.method == 'POST':
        
        form=addteacher_form(request.POST)
        print(form.errors)
        if form.is_valid():
           
            instance = form.save(commit=False)
            instance.owner=request.user
            instance.save()
            
        return redirect('/')


    


def createteacher(request):
    return render(request, 'createteacher.html')


def addstudent(request):
    return render(request, 'addstudent.html')


def addstudent_registerd_cources(request):
    return render(request, 'addstudent_registerd_cources')


def addstudent1(request):
    pass

def addstubject(request):
    return render(request, 'addsubject.html')


def addsubject1(request):
    if request.method == 'POST':
        
        form=addsubject_form(request.POST)
        print(form.errors)
        if form.is_valid():
            instance = form.save(commit=False)
            
            instance.save()
            return render(request, 'addsubject.html')
        else:
            print('error')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')



def addsubject(request):
    return render(request, 'addsubject.html')
