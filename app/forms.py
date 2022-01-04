from django.forms import ModelForm
from app.models import Clientes

# Create the form class.
class ClientesForm(ModelForm):
  class Meta:
    model = Clientes
    fields = ['nome', 'email', 'telefone', 'endereco', 'bairro', 'cidade', 'cep']