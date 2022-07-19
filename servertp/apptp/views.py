from distutils.log import info
from django.http import HttpResponse
from django.shortcuts import render
from apptp.models import Empresa, Empleado, Producto
from apptp.forms import Empleado_formulario, Empresa_formulario, Producto_formulario


# Create your views here.
def inicio(request):
    context = {}
    return render(request, 'base.html', context)

def empresa_formulario(request):

    if request.method == 'POST':

        miformularioEmpresa = Empresa_formulario(request.POST)

        if miformularioEmpresa.is_valid():

            informacion = miformularioEmpresa.cleaned_data  

            empresa = Empresa(empresa=informacion['empresa'], dedicacion=informacion['dedicacion'])

            empresa.save() #La informacion se manda a la base de datos y se queda ahi, se puede ver reflejado en el admin 

            return render(request, 'gracias.html') #HTML de gracias

    else:

        miformularioEmpresa = Empresa_formulario()
    
    return render(request, 'empresa.html', {'miformularioEmpresa':miformularioEmpresa})

def producto_formulario(request):

    if request.method == 'POST':

        miformularioProducto = Producto_formulario(request.POST)

        if miformularioProducto.is_valid():

            informacion = miformularioProducto.cleaned_data

            producto = Producto(nombre_producto=informacion['nombre_producto'], producto_empresa=informacion['producto_empresa'])

            producto.save()

            return render(request, 'gracias.html')

    else:

        miformularioProducto = Producto_formulario()
    
    return render(request, 'producto.html', {'miformularioProducto':miformularioProducto})

def empleado_formulario(request):

    if request.method == 'POST':

        miformularioEmpleado = Empleado_formulario(request.POST)

        if miformularioEmpleado.is_valid():

            informacion = miformularioEmpleado.cleaned_data

            empleado = Empleado(nombre_completo=informacion['nombre_completo'], puesto=informacion['puesto'], empresa_trabajo=informacion['empresa_trabajo'])

            empleado.save()

            return render(request, 'gracias.html')

    else:

        miformularioEmpleado = Empleado_formulario()

    return render(request, 'empleado.html', {'miformularioEmpleado':miformularioEmpleado})

def busqueda_producto(request):

    return render(request, "busqueda_productos.html")

def busqueda_empleados(request):

    return render(request, 'busqueda_empleados.html')

def resultado_producto(request):

    if request.GET['nombre_producto']: # [va la caracteristica que va en el model]

        producto = request.GET['nombre_producto'] # [va la caracteristica que va en el model]

        productos = Producto.objects.filter(nombre_producto__icontains=producto) # icontains sirve para ver lo que contiene la variable que se le asigne

        return render(request, 'resultado_busqueda_productos.html', {'productos':productos, 'producto':producto})

    else:

        mensaje = 'mensaje.html'

    return render(request, mensaje)

def resultado_persona(request):

    if request.GET['nombre_completo']: #Esta busqueda que realiza la funcion es solo con el nombre

        empleado = request.GET['nombre_completo']

        empleados = Empleado.objects.filter(nombre_completo__icontains=empleado)

        return render(request, 'resultado_busqueda_empleado.html', {'empleados':empleados, 'empleado':empleado})

    else:

        mensaje = 'mensaje.html'

    return render(request, mensaje)