from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse

# Create your views here.
    
    
def prueba(request):
    
    return render(request,"App1/index.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "App1/login.html")
    else:
        form = UserCreationForm()
    return render(request, "App1/register.html", {"form":form})