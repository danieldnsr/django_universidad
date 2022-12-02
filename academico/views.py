from django.shortcuts import render, redirect, get_object_or_404
from academico.models import Facultad, Carrera, Curso
from academico.forms import *
from datetime import datetime

menu = ["Carreras", "Facultades", "Cursos"]

def principal(request):
    fecha = datetime.now()
    
    context = {
        "fecha" : fecha,
        "menu" : menu
    }
    return render(request, "base.html", context)
# Create your views here.
def facultades(request):
    fecha = datetime.now()
    query = request.GET.get('query')
    if query == None:
        facultades = Facultad.objects.all()
        context = {
            "fecha": fecha,
            "facultades" : facultades,
            "menu" : menu,
        }
    else :
        facultad_q = Facultad.objects.filter(name__icontains=query)
        context = {
            "facultades_q": facultad_q,
            "menu" : menu,
        }
    context["fecha"] = fecha
    return render(request, "facultades.html", context=context)

def carreras(request):
    fecha = datetime.now()
    carreras = Carrera.objects.all()
    #contexto
    context = {
        "fecha" : fecha,
        "carreras" : carreras,
        "menu" : menu,
    }
    return render(request, "carreras.html", context)

def c_facultades(request):
    if request.method == "POST":
        form = FacultadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultades')
        else :
            form = FacultadForm()
            model = "FACULTADES"
            message = "Ha ocurrido un error gravisimo, aprenda a escribir!"
            context = {"form" : form, "model": model, "message" : message, "menu" : menu}
            return render(request, "create_form.html", context)
    else:
        form = FacultadForm()
        model = "FACULTADES"
    context = {"form" : form, "model": model, "menu" : menu}
    return render(request, "create_form.html", context)

def c_carreras(request):
    if request.method == "POST":
        form = CarrerasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carreras')
        else :
            form = CarrerasForm()
            model = "CARRERAS"
            message = "Ha ocurrido un error gravisimo, aprenda a escribir!"
            context = {"form" : form, "model": model, "message" : message, "menu" : menu}
            return render(request, "create_form.html", context)
    else:
        form = CarrerasForm()
        model = "CARRERAS"
    context = {"form" : form, "model": model, "menu" : menu}
    return render(request, "create_form.html", context)

#############################################################################

def curso(request):
    fecha = datetime.now()
    query = request.GET.get("query")
    if not query:
        context = {
            "fecha" : fecha,
            "menu" : menu,
        }
        return render(request, "cursos.html", context)
    else:
        id = Carrera.objects.get(name=query)
        cursos = Curso.objects.filter(degree__exact=id.id)
        context = {
            "fecha" : fecha,
            "menu" : menu,
            "cursos" : cursos
        }
        return render(request, "cursos.html", context)

def u_cursos(request, id_curso):
    curso_u = get_object_or_404(Curso, id = int(id_curso))

    if request.method == "GET":
        fecha = datetime.now()
        form = CursosForm(instance=curso_u)
        d_url = "d_curso"

        context = {
            "fecha" : fecha,
            "menu" : menu,
            "form" : form,
            "d_url" : d_url,
            "id_curso" : id_curso
        }
        return render(request, "create_form.html", context)
    else:
        form = CursosForm(request.POST, instance=curso_u).save()
        return redirect("cursos")


def c_cursos(request):
    if request.method == "GET":
        fecha = datetime.now()
        form = CursosForm()
        context = {
            "fecha" : fecha,
            "menu" : menu,
            "form" : form
        }
        return render(request, "create_form.html", context)
    else:
        form = CursosForm(request.POST).save()
        return redirect("cursos")

def d_cursos(request, id_curso):
    curso_d = get_object_or_404(Curso, id = int(id_curso))
    curso_d.delete()
    return redirect("cursos")
    


