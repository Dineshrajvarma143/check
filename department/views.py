from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from department.models import *
from django.contrib import messages

# Create your views here.
def homep(request):
    results=list(EEE.objects.all()[::-1])[0:6]
    if request.method=="POST":
        obj=EEE.objects.all()
        return render(request,'home.html',{'res':obj})
    return render(request,'home.html',{'res':results})

def aboutp(request):
    return render(request,'about.html')

def contactp(request):
    return render(request,'contact.html')

def profilep(request):
    return render(request,'profile.html')

def loginp(request):
    if request.method=="POST":
        studentname=request.POST.get('uname')
        mail=request.POST.get('mail')
        if "@srit.ac.in" in mail:
            obj=authenticate(request,username=studentname,email=mail,)
            if obj:
                login(request,obj)
                return redirect('homepage')
            messages.warning(request,"not valid crendentials!")
            return redirect('homepage')
    return render(request,'login.html')

def registerp(request):
    if request.method=="POST" and request.user.is_staff:
        pinno=request.POST.get('uname')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        mail=request.POST.get('mail')
        department=request.POST.get('branch')
        Ryear=request.POST.get('year')
        contact=request.POST.get('phone.no')
        currentrole=request.POST.get('rolee')

        cand = User.objects.create_user(username=pinno,first_name=fname,last_name=lname,email=mail,password="moddhu")
        cand.save()
        pers=Booking(staff=cand,department=department,Ryear=Ryear,contact=contact,currentrole=currentrole)
        pers.save()
        return redirect('loginpage')
    return render(request,'register.html')

def batchp(request):
    if request.method=='POST':
        ptitle=request.POST.get('protitle')
        pmembers=request.POST.get('members')
        pdescription=request.POST.get('story')
        pguide=request.POST.get('mentor')
        pdomain=request.POST.get('domain')
        mam=EEE(ptitle=ptitle,pmembers=pmembers,pdescription=pdescription,pguide=pguide,pdomain=pdomain)
        mam.save()
        return redirect('profilepage')
    return render(request,'more.html')
def singlep(request):
    results=EEE.objects.all()[::-1]
    return render(request,'profile.html',{'res':results})

def logoutp(request):
    logout(request)
    return redirect('loginpage')


@login_required(login_url='loginPage')
def deletep(request,rid):
    if request.user.is_staff:
        obj=EEE.objects.get(id=rid)
        usr_id=obj.person.id
        obj2=User.objects.get(id=usr_id)
        obj.delete()
        obj2.delete()
        return redirect('staffpage')
    else:
        return redirect('homepage')
def displayp(request,rid):
    b=EEE.objects.get(id=rid)
    if request.method=="POST":
        b.post=request.POST.get('desc')
        b.save()
    return render(request,'single.html',{'res':b})

@login_required(login_url='loginpage')
def updatep(request,rid):
    if request.user.is_staff:
        if request.method=="POST":
            obj=EEE.objects.get(id=rid)
            obj.ptitle=request.POST.get('protitle')
            obj.pmembers=request.POST.get('members')
            obj.pdescription=request.POST.get('story')
            obj.pguide=request.POST.get('mentor')
            obj.pdomain=request.POST.get('domain')
            obj.save()
            return redirect('homepage')
        if EEE.objects.filter(id=rid).exists():
            obj=EEE.objects.get(id=rid)
            return render(request,'update.html',{'res':obj})
        return redirect('profilepage')
    return redirect("homepage")

def batch1p(request):
    if request.method=="POST":
        obj=EEE.objects.filter(pyear=2021).exists()
        obj.save()
        print(obj)
    return render(request,'batch2021.html',{"res":obj})
def batch2p(request):
    if request.method=="POST":
        obj=EEE.objects.filter(pyear=2022).exists()
        obj.save()
        
    return render(request,'batch2022.html',{"res":obj})
def batch3p(request):
    if request.method=="POST":
        obj=EEE.objects.filter(pyear=2023).exists()
        obj.save()
        
    return render(request,'batch2023.html',{"res":obj})





    



    

