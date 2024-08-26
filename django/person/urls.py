from django.urls import path
from person.views import PessoaListView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView

urlpatterns = [
    path('', PessoaListView.as_view(), name="list"),
    path('create/', PessoaCreateView.as_view(), name="create"),
    path('update/<int:pk>/', PessoaUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PessoaDeleteView.as_view(), name='delete'),
]
