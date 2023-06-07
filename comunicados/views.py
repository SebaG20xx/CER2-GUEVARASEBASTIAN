from django.shortcuts import render, redirect, get_object_or_404
from .models import Comunicado, Categoria
from .forms import ComunicadoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse

def index(request):

    """
    Vista para mostrar la página principal que lista todos los comunicados.

    - Obtiene todos los comunicados.
    - Filtra por nivel si se especifica.
    - Filtra por categoría si se especifica.
    - Obtiene todas las categorías.

    Retorna la respuesta renderizada con el contexto en la plantilla 'comunicados/index.html'.
    """

    comunicados = Comunicado.objects.all()
    nivel = request.GET.get('nivel')
    categoria_id = request.GET.get('categoria')
    if nivel:
        comunicados = comunicados.filter(nivel=nivel)

    if categoria_id:
        categoria = Categoria.objects.get(id=categoria_id)
        comunicados = comunicados.filter(categoria=categoria)

    categorias = Categoria.objects.all()

    context = {
        'comunicados': comunicados,
        'categorias': categorias,
    }
    return render(request, 'comunicados/index.html', context)


@login_required
def registrar_comunicado(request):
    """
    Vista para registrar un nuevo comunicado.
    
    - Obtiene la fecha actual.
    - Si el método de solicitud es POST, procesa el formulario enviado y guarda el comunicado.
    - Si el método de solicitud es GET, muestra el formulario de registro de comunicado.
    
    Retorna la respuesta renderizada con el contexto en la plantilla 'comunicados/registrar_comunicado.html'.
    """
    fecha_actual = timezone.now().date()
    
    if request.method == 'POST':
        form = ComunicadoForm(request.POST)
        if form.is_valid():
            comunicado = form.save(commit=False)
            comunicado.publicado_por = request.user
            comunicado.save()
            messages.success(request, 'Comunicado registrado exitosamente.')
            return redirect('index')
    else:
        form = ComunicadoForm()
    
    context = {
        'fecha_actual': fecha_actual,
        'form': form,
    }
    return render(request, 'comunicados/registrar_comunicado.html', context)

@login_required
def edit_comunicado(request, comunicado_id):
    comunicado = get_object_or_404(Comunicado, id=comunicado_id)
    if request.method == 'POST':
        form = ComunicadoForm(request.POST, instance=comunicado)
        if form.is_valid():
            form.save()
    else:
        form = ComunicadoForm(instance=comunicado)
    
    context = {'form': form}
    return render(request, 'comunicados/edit_comunicado.html', context)
