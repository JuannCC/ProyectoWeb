from django.shortcuts import render
from blog.models import Post, Categoria
# Create your views here.

def blog(request):
    #importa todos los servicios
    posts=Post.objects.all()
    return render(request,"blog/blog.html", {"posts": posts})

def categoria(request, categoria_id):
    #importa todos los servicios
    categoria= Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)

    return render(request,"blog/categoria.html", {"categoria": categoria, "posts": posts})