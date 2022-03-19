from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.

def blog(request):
    post = Post.objects.all()
    return render(request, "blog/blog.html" , {"post": post})

def categoria(request, categoria_id):
    categoria= Categoria.objects.get(id= categoria_id) # creo la variable categoria para que me filtre o me triga los datos
    posts = Post.objects.filter(categorias = categoria) # filter para que me traiga los posts filtrados, y uso categoria de arriba
    return render(request, "blog/categoria.html", {'categoria': categoria, 'post': posts})

