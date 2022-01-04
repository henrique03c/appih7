from django.shortcuts import redirect, render
from app.forms import ClientesForm
from app.models import Clientes

# Create your views here.
def home(request):
  data = {}
  search = request.GET.get('search')
  if search:
    data['db'] = Clientes.objects.filter(nome__icontains=search)
  else:
    data['db'] = Clientes.objects.all()
  return render(request, 'index.html', data)

def cadastro(request):
  data = {}
  data['form'] = ClientesForm()
  return render(request, 'cadastro.html', data)

def create(request):
  form = ClientesForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('home')

def vizualizar(request, pk):
  data = {}
  data['db'] = Clientes.objects.get(pk=pk)
  return render(request, 'vizualizar.html', data)

def editar(request, pk):
  data = {}
  data['db'] = Clientes.objects.get(pk=pk)
  data['form'] = ClientesForm(instance=data['db'])
  return render(request, 'cadastro.html', data)

def alterar(request, pk):
  data = {}
  data['db'] = Clientes.objects.get(pk=pk)
  form = ClientesForm(request.POST or None, instance=data['db'])
  if form.is_valid():
    form.save()
    return redirect('home')

def deletar(request, pk):
  db = Clientes.objects.get(pk=pk)
  db.delete()
  return redirect('home')