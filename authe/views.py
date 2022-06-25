from django.shortcuts import redirect, render
from django.views.generic import CreateView,View
from authe.models import registermodel
from authe.forms import registerform
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

class registerview(CreateView):
    template_name="register.html"
    model=registermodel
    form_class=registerform
    success_url='/success/'
    def get_queryset(self):
        user=super().get_queryset()
        user.password=make_password(self.cleaned_date['password'])

class loginview(View):
    def get(self,request):
        form=AuthenticationForm
        return render(request,"login.html",{"form":form})
    def post(self,request):
        print(request.POST)
        user=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(username=user,password=password)
        if user is not None:
            login(request,user)
            return redirect("/success/")

@login_required(login_url='/login')
def logoutview(request):
    logout(request)
    return redirect("/login/")

@login_required(login_url='/login')
def  successview(request):
    return render(request,"success.html")

    