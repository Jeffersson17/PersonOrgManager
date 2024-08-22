from django.urls import path
from .views import home, PessoaListView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView

urlpatterns = [
    path('', home),
    path('pessoa/', PessoaListView.as_view(), name="pessoa_list"),
    path('create/', PessoaCreateView.as_view(), name="create"),
    path('editar/<int:pk>/', PessoaUpdateView.as_view(), name='editar'),
    path('delete/<int:pk>/', PessoaDeleteView.as_view(), name='delete'),
]
