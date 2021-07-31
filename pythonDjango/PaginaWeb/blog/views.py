from django.shortcuts import render
from blog.models import post, categoria

# Create your views here.

def blog(request):
    posts=post.objects.all()
    return render(request, "blog/blog.html",{'posts':posts})

def categoriaMethod(request, categoria_id):
    categ=categoria.objects.get(id=categoria_id)
    posts=post.objects.filter(categoria=categ)
    return render(request, "blog/categoria.html",{'categorias':categ, 'posts':posts})
