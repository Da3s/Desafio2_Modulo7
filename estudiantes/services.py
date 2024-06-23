from .models import Curso, Profesor, Direccion, Estudiante


def crear_curso(pCodigo, pNombre, pVersion):
    curso= Curso(codigo= pCodigo, nombre= pNombre, version= pVersion)
    curso.save()
    return curso
    
    
def crear_profesor(pRut, pNombre, pApellido, pCreado_por):
    profesor = Profesor(rut= pRut, nombre= pNombre, apellido= pApellido, creado_por= pCreado_por)
    profesor.save()
    return profesor
    

def crear_estudiante(pRut, pNombre, pApellido, pFecha_nac, pCreado_por):
    estudiante = Estudiante(rut= pRut, nombre= pNombre, apellido= pApellido, fecha_nac= pFecha_nac, creado_por= pCreado_por)
    estudiante.save()
    return estudiante
    
    
def crear_direccion(pCalle, pNumero, pDepto, pComuna, pCiudad, pRegion,rut_estudiante):
    estudiante = Estudiante.objects.get(rut= rut_estudiante)
    direccion = Direccion(calle=pCalle, numero=pNumero, depto=pDepto, comuna= pComuna, ciudad= pCiudad, region= pRegion, estudiante= estudiante)
    direccion.save()
    return direccion
    
    
def obtiene_estudiante(pRut):
    return Estudiante.objects.get(rut= pRut) # puede ser de esta forma tambien el retorno


def obtiene_profesor(pRut):
    profesor = Profesor.objects.get(rut= pRut)
    return profesor


def obtiene_curso(pCodigo):
    curso = Curso.objects.get(codigo= pCodigo)
    return curso


def agrega_profesor_a_curso(oCodigo_curso, oRut_profe):
    curso = Curso.objects.get(codigo= oCodigo_curso)
    profesor = Profesor.objects.get(rut= oRut_profe)
    profesor.cursos.add(curso)
    return curso



def agrega_cursos_a_estudiante(oCursos, oRut_estudiante):
    #fk la tiene el estudiante asi que se parte por el 
    estudiante = Estudiante.objects.get(rut= oRut_estudiante)
    curso = Curso.objects.get(codigo= oCursos)
    estudiante.cursos.add(curso)    
    return curso


def imprime_estudiante_cursos(pRut):
    estudiante = Estudiante.objects.get(rut= pRut)
    cursos = estudiante.cursos.all()
    return cursos