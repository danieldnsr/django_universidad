"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from academico.views import *
from login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("princial/", principal, name="principal"),
    path("", login, name="login"),
    path("facultades/", facultades, name="facultades"),
    path("cursos/", curso, name="cursos"),
    path("carreras/", carreras, name="carreras"),
    path("create/facultades", c_facultades, name = "c_facultades"),
    path("create/carreras", c_carreras, name = "c_carreras"),
    path("create/cursos", c_cursos, name="c_cursos"),
    path("update/cursos/<id_curso>", u_cursos, name="u_cursos"),
    path("delete/cursos/<id_curso>", d_cursos, name="d_curso"),
]
