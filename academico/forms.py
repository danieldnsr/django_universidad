from django.forms import * 
from academico.models import Facultad, Carrera, Curso

class FacultadForm(ModelForm):
    class Meta:
        model = Facultad
        fields = "__all__"
    
class CarrerasForm(ModelForm):
    class Meta:
        model = Carrera
        fields = "__all__"

class CursosForm(ModelForm):
    class Meta:
        widgets = {'begin': DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Fecha Inicio', 'type':'date'}),
                    'end' : DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Fecha Fin', 'type':'date'})}
        model = Curso
        fields = "__all__"

