from django.shortcuts import render
from .models import Board, Post, Reply
from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Post
from .forms import PostForm, RespuestaForm,BoardForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseServerError

@login_required
@require_http_methods(["GET"])
def foro_inicio(request):
    
    if request.method == 'GET':
        boards_general = Board.objects.filter(categoria='general')
        boards_tecnologia = Board.objects.filter(categoria='tecnologia')
        boards_spiderman = Board.objects.filter(categoria='spiderman')
        ultimos_posts = Post.objects.order_by('-fecha_creacion')[:10]
        imagenes_recientes = Post.objects.exclude(imagen='').order_by('-fecha_creacion')[:5]
        
        context = {
            'user': request.user,
            'boards_general': boards_general,
            'boards_tecnologia': boards_tecnologia,
            'boards_spiderman': boards_spiderman,
            'ultimos_posts': ultimos_posts,
            'imagenes_recientes': imagenes_recientes,
        }
        return render(request, 'forum/foro_inicio.html', context)

    return HttpResponse("Metodo no permitido", status=405)


@login_required
@require_http_methods(["GET", "POST"])
def ver_board(request, slug):

    if not request.user.has_perm('forum.view_board'):
        return render(request, "403.html")

    
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.post = get_object_or_404(Post, id=post_id)
            respuesta.autor = request.user
            respuesta.save()
            return redirect('ver_board', slug=slug)
    else:
        form = RespuestaForm()

    if request.method == 'GET':
        board = get_object_or_404(Board, slug=slug)
        posts = Post.objects.filter(board=board).order_by('-fecha_creacion')

        return render(request, 'forum/ver_board.html', {
            'board': board,
            'posts': posts,
            'form': form
        })
    
    return HttpResponse("Metodo no permitido", status=405)

@login_required
@require_http_methods(["GET", "POST"])
def crear_post(request, slug):

    if not request.user.has_perm('forum.add_post'):
        return render(request, "403.html")

    if request.method == 'GET':

        board = get_object_or_404(Board, slug=slug)
        form = PostForm()

        return render(request, 'forum/crear_post.html', {
        'board': board,
        'form': form
        })

    if request.method == 'POST':
        board = get_object_or_404(Board, slug=slug)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.board = board
            post.save()
            return redirect('ver_board', slug=board.slug)
       

    return HttpResponse("Metodo no permitido", status=405)
    


@login_required
@require_http_methods(["GET", "POST"])
def crear_board(request):

    if not request.user.has_perm('forum.add_board'):
        return render(request, "403.html")

    if request.method == 'GET':
        form = BoardForm()
        return render(request, 'forum/crear_board.html', {'form': form})

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('foro_inicio')  # Redirige a donde veas conveniente
    
    return HttpResponse("Metodo no permitido", status=405)


@login_required
def eliminar_post(request, post_id):
    if not request.user.has_perm('forum.delete_post'):
        return render(request, "403.html")

    try:
        post = get_object_or_404(Post, id=post_id)
        board_slug = post.board.slug
        post.delete()
        return redirect('ver_board', board_slug)
    except Post.DoesNotExist:
        return render(request, "404.html", {"mensaje": "El post no existe."})
    except Exception as e:
        print(f"Error al eliminar el post: {e}")
        return HttpResponseServerError("Ocurrió un error al intentar eliminar el post.")

@login_required
def banear_usuario(request, user_id):
    if not request.user.has_perm('forum.delete_post'):
        return render(request, "403.html")

    try:
        user = get_object_or_404(User, id=user_id)
        user.is_active = False
        user.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    except User.DoesNotExist:
        return render(request, "404.html", {"mensaje": "El usuario no existe."})
    except Exception as e:
        print(f"Error al banear usuario: {e}")
        return HttpResponseServerError("Ocurrió un error al intentar banear al usuario.")

@login_required
def eliminar_respuesta(request, respuesta_id):
    if not request.user.has_perm('forum.delete_reply'):
        return render(request, "403.html")

    try:
        respuesta = get_object_or_404(Reply, id=respuesta_id)
        board_slug = respuesta.post.board.slug
        respuesta.delete()
        return redirect('ver_board', board_slug)
    except Reply.DoesNotExist:
        return render(request, "404.html", {"mensaje": "La respuesta no existe."})
    except Exception as e:
        # Para desarrollo: imprime el error o loguéalo
        print(f"Error al eliminar la respuesta: {e}")
        return HttpResponseServerError("Ocurrió un error al intentar eliminar la respuesta.")