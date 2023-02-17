from django.shortcuts import render, redirect
from .forms import FormularioContacto

# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContacto()

    # Si el metodo es POST que me guarde en formulario_contacto lo que enviamos. Si los campos son validos
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            return redirect("/contacto/?valido")


    return render(request,"contacto/contacto.html", {'miformulario':formulario_contacto})