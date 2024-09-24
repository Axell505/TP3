from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Post
from .forms import PostForm

# 1. Listar todas las publicaciones
def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')  # Ordenar por fecha de publicación descendente
    return render(request, 'post_list.html', {'posts': posts})

# 2. Crear una nueva publicación
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form, 'action': 'Crear Publicación'})

# 3. Ver el detalle de una publicación específica
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})

# 4. Editar una publicación existente
@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author != request.user:
        return redirect('post_detail', id=post.id)  # Evita que otros editen el post
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form, 'action': 'Editar Publicación'})

# 5. Eliminar una publicación
@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author != request.user:
        return redirect('post_detail', id=post.id)  # Evita que otros eliminen el post
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})

# 6. Registrar un nuevo usuario
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('post_list')  # Redirige a la lista de publicaciones
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
