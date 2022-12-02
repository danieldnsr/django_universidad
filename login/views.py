from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm

# Create your views here.
def login(request):
    
    if request.method == "GET":
        form = LoginForm()
        context = {
            "form" : form,
        }
        return render(request, "create_form_login.html", context)
    else:
        user = request.POST.get("usuario")
        password = request.POST.get("contrasenia")
        user_auth = authenticate(username = user, password = password)
        if user_auth:
            login(request, user_auth)
            return redirect("cursos")
        else:
            warning_str = "No se encontro el usuario"
            context = {
                "warning_str" : warning_str
            }
            return render(request, "create_form_login.html", context)