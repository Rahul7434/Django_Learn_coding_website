from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import SignUpForm, ProfileForm,ContactForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'formsapp/index.html')

def signup(request):
    if request.method == "POST":
        fm= SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Your Account has been Created !! Now You can Login')
        else:
            messages.error(request,'Incorect!!!')
    else:
        fm=SignUpForm()   
    return render(request,'formsapp/signup.html',{'form':fm})
       
def cources(request):
    return render(request,'formsapp/cources.html')

def login_fun(request):
    if request.method =="POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user =authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Login Successfully..!')
                return HttpResponseRedirect('/profile/')
        else:
            messages.error(request,'Invalid Form Data Please Sign-Up !!!')      
    else:
        fm=AuthenticationForm()  
    return render(request,'formsapp/login.html',{'form':fm})

def services(request):
    return render(request,'formsapp/services.html')

def aboutus(request):
    return render(request,'formsapp/aboutus.html')

def contactus(request):
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
            subject = "Website Inquiry"
            body ={
                'name': fm.cleaned_data['name'],
                'email':fm.cleaned_data['email'],
                'message':fm.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            
            try:
                send_mail(subject,message,'rahuljadhav1672@gmail.com',['rahuljadhav1672@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Invalid Header Found") 
            return redirect("main:homepage")
    fm = ContactForm()
    return render(request,'formsapp/contactus.html',{'form':fm})

# Profile Page
def profile(request):
   if request.user.is_authenticated:
        fm = ProfileForm(instance=request.user) 
        return render(request,'formsapp/profile.html',{'name':request.user,'form':fm})
   else:
       return HttpResponseRedirect('/login/')
    
# logout Function 
def logout_user(request):
    logout(request)
    messages.success(request,'logout Successfully..')
    return HttpResponseRedirect('/login/')


# Change Password With old password 
def changepass(request):
    if request.user.is_authenticated:    
        if request.method=='POST':
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request.fm.user)
                messages.success(request,'Password chnaged Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'formsapp/changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
    
