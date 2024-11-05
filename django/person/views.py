from django.urls import reverse_lazy
from .models import Pessoa
from .forms import PessoaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets, generics
from .serializers import PessoaSerializer


class PessoaListView(ListView):
    model = Pessoa
    template_name = "pessoa/person_list.html"


class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = "pessoa/create.html"
    success_url = reverse_lazy("list-person-api")


class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'pessoa/update.html'
    success_url = reverse_lazy("person_list")


class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = reverse_lazy("person_list")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class PessoaListAPIView(generics.ListAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class PessoaCreateAPIView(generics.CreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
