from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import SpidermanVariant
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django import forms
from django.views.decorators.http import require_http_methods

@login_required
@require_http_methods(["GET"])
def home(request):
    if not request.user.has_perm('main.view_spidermanvariant'):
        return render(request, "403.html")

    if request.method == 'GET':
        nombre = request.GET.get('q', '')
        descripcion = request.GET.get('descripcion', '')
        orden = request.GET.get('orden', 'asc')
        cantidad = request.GET.get('cantidad', 6)  # Valor por defecto: 6 elementos por página

        queryset = SpidermanVariant.objects.all()

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if descripcion:
            queryset = queryset.filter(descripcion__icontains=descripcion)

        if orden == 'asc':
            queryset = queryset.order_by('nombre')
        elif orden == 'desc':
            queryset = queryset.order_by('-nombre')

        paginator = Paginator(queryset, int(cantidad))
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'home.html', {
            'page_obj': page_obj,
            'nombre': nombre,
            'descripcion': descripcion,
            'orden': orden,
            'cantidad': cantidad
        })
    
    return HttpResponse("Metodo no permitido", status=405)

@login_required
@require_http_methods(["GET"])
def admin_only_view(request):
    if not request.user.has_perm('main.add_spidermanvariant'):
        return render(request, "403.html")
    
    if request.method == 'GET':
        nombre = request.GET.get('q', '')
        descripcion = request.GET.get('descripcion', '')
        orden = request.GET.get('orden', 'asc')
        cantidad = request.GET.get('cantidad', 6)  # Valor por defecto: 6 elementos por página

        queryset = SpidermanVariant.objects.all()

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if descripcion:
            queryset = queryset.filter(descripcion__icontains=descripcion)

        if orden == 'asc':
            queryset = queryset.order_by('nombre')
        elif orden == 'desc':
            queryset = queryset.order_by('-nombre')

        paginator = Paginator(queryset, int(cantidad))
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'admin_template.html', {
            'page_obj': page_obj,
            'nombre': nombre,
            'descripcion': descripcion,
            'orden': orden,
            'cantidad': cantidad
        })
    
    return HttpResponse("Metodo no permitido", status=405)



@login_required
@require_http_methods(["POST"])
def eliminar_variant(request, id):

    if not request.user.has_perm('main.delete_spidermanvariant'):
        return render(request, "403.html")

    variant = get_object_or_404(SpidermanVariant, id=id)
    if request.method == "POST":
        variant.delete()
        messages.success(request, "Variante eliminada correctamente.")
        return redirect('admin_only')
    
    return HttpResponse("Metodo no permitido", status=405)
    
# Editar SpiderMan Cards

class SpidermanForm(forms.ModelForm):
    class Meta:
        model = SpidermanVariant
        fields = ['imagen', 'nombre', 'datos', 'descripcion']

@login_required
@require_http_methods(["POST", "GET"])
def editar_variant(request, id):
    if not request.user.has_perm('main.change_spidermanvariant'):
        return render(request, "403.html")
    
    if request.method == "GET":

        variant = get_object_or_404(SpidermanVariant, pk=id)

        return render(request, 'editar_variant.html', {'variant': variant})
    
    if request.method == 'POST':
                variant = get_object_or_404(SpidermanVariant, pk=id)
                variant.imagen = request.POST['imagen']
                variant.nombre = request.POST['nombre']
                variant.descripcion = request.POST['descripcion']
                variant.save()
                return redirect('admin_only')

    return HttpResponse("Metodo no permitido", status=405)


# Agregra Elemento
@login_required
@require_http_methods(["POST"])
def agregar_variant(request):
    if not request.user.has_perm('main.add_spidermanvariant'):
            return render(request, "403.html")

    if request.method == "POST":
        
        imagen = request.POST.get("imagen")
        nombre = request.POST.get("nombre")
        datos = request.POST.get("datos")
        descripcion = request.POST.get("descripcion")

        SpidermanVariant.objects.create(
            imagen=imagen,
            nombre=nombre,
            datos=datos,
            descripcion=descripcion
        )
        return redirect("admin_only")
    
    return HttpResponse("Metodo no permitido", status=405)
    
@login_required
@require_http_methods(["POST", "GET"])
def user_profile(request):

    if request.method == 'GET':
       
        return render(request, 'user_profile.html')
    
    if request.method == 'POST':
        print("Por aqui paso verdad?")
        new_username = request.POST.get('username')
        new_avatar = request.FILES.get('avatar')

        print(new_avatar)

        user = request.user
        if new_username:
            user.username = new_username
            user.save()
        if new_avatar:
            print("Por aqui paso")
            user.profile.avatar = new_avatar  # Asegúrate que tengas un modelo `Profile` con campo `avatar`
            user.profile.save()

        return redirect('home')  # O a donde necesites
    
    return HttpResponse("Metodo no permitido", status=405)
