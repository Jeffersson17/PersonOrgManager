from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Organization
from .forms import OrganizationForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrganizationSerializer, StatusChoicesSerializer
from django.urls import reverse_lazy
from address.defaults import STATE_CITY_CHOICE, ADDRESS_TYPE, AREA_CHOICES
from rest_framework import generics, viewsets
from .filters import OrganizationFilter


class OrganizationListView(ListView):
    model = Organization
    template_name = 'register/list_organization.html'


class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "register/register_organization.html"
    success_url = reverse_lazy("list_organization")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['states'] = STATE_CITY_CHOICE
        context['address_type'] = ADDRESS_TYPE
        context['area'] = AREA_CHOICES
        return context


class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'actions/update.html'
    success_url = reverse_lazy("list_organization")


class OrganizationDeleteView(DeleteView):
    model = Organization
    success_url = reverse_lazy("list_organization")


    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filterset_class = OrganizationFilter


class StatusChoices(APIView):
    def get(self, request):
        data = {
            "area_choices": AREA_CHOICES,
            "address_type": ADDRESS_TYPE,
            "state_city_choice": STATE_CITY_CHOICE,
        }
        serializer = StatusChoicesSerializer(data)
        return Response(serializer.data)


class OrganizationListAPIView(generics.ListAPIView):
    queryset = Organization.objects.all().order_by('id')
    serializer_class = OrganizationSerializer


class OrganizationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
