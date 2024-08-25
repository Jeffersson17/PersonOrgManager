from django.urls import reverse_lazy
from .models import Pessoa
from .forms import PessoaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class PessoaListView(ListView):
    model = Pessoa
    template_name = "pessoa/listagem_pessoas.html"


class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = "pessoa/create.html"
    success_url = "/core/pessoa"


class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'pessoa/update.html'
    success_url = '/core/pessoa'


class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = reverse_lazy("pessoa_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
