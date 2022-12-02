from django.db import models

# Create your models here.

#FACULTADES
class Facultad(models.Model):
    id = models.BigAutoField(verbose_name = "CODIGO", primary_key = True)
    name = models.CharField(verbose_name = "NOMBRE", max_length=40)
    description = models.CharField(verbose_name = "RESUMEN", max_length=200)
    dean = models.CharField(verbose_name = "DECANO", max_length=200)
    secretary = models.CharField(verbose_name = "SECRETARIA", max_length=200)

    def __str__(self) -> str:
        return str(self.name)

#CARRERAS
class Carrera(models.Model):
    id = models.BigAutoField(verbose_name = "CODIGO", primary_key = True)
    name = models.CharField(verbose_name = "CARRERA", max_length=40)
    description = models.CharField(verbose_name = "RESUMEN", max_length=200)
    credits = models.PositiveSmallIntegerField(verbose_name = "CREDITOS")
    faculty = models.ForeignKey(Facultad, on_delete = models.CASCADE, verbose_name="FACULTAD")

    def __str__(self) -> str:
        return str(self.name)

#DOCENTES
class Docente(models.Model):
    id = models.BigAutoField(verbose_name = "CODIGO", primary_key = True)
    name = models.CharField(verbose_name = "NOMBRE", max_length=40)
    lastname = models.CharField(verbose_name = "APELLIDO", max_length=40)
    document = models.PositiveIntegerField(verbose_name="CEDULA", unique=True)
    mail = models.EmailField(verbose_name="CORREO")

    def __str__(self) -> str:
        return str(self.name)

#CURSOS
class Curso(models.Model):
    id = models.BigAutoField(verbose_name = "CODIGO", primary_key = True)
    name = models.CharField(verbose_name = "CURSO", max_length = 30)
    description = models.CharField(verbose_name = "RESUMEN", max_length=200, blank=True, null=True)
    begin = models.DateField(verbose_name="Fecha inicio")
    end = models.DateField(verbose_name="Fecha terminacion")
    credits = models.PositiveSmallIntegerField(verbose_name="CREDITOS")
    teacher = models.ForeignKey(Docente, blank = True, null = True, on_delete=models.SET_NULL)
    schedulers = [("D", "DIURNO"), ("N", "NOCTURNO"), ("FDS", "FIN DE SEMANA")]
    scheduler = models.CharField(verbose_name="JORNADA", max_length=3, choices=schedulers)
    degree = models.ForeignKey(Carrera, on_delete=models.CASCADE)