from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import UsuarioForm
from .models import Producto

def register(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UsuarioForm()
    return render(request, 'djangoAuthApp/render.html', {'form': form})

class ProductoListView(ListView):
    template_name = 'djangoAuthApp/success.html'
    context_object_name = 'productos'
    paginate_by = 10

    def get_queryset(self):
        productos_query = Producto.objects.all()
        for producto in productos_query:
            print(producto)
        return productos_query.order_by('id')
    
def success(request):
    return render(request, 'djangoAuthApp/success.html')