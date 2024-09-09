from django.views.generic import CreateView, ListView
from .models import Organization
from .forms import OrganizationForm
from django.urls import reverse_lazy
from address.defaults import STATE_CITY_CHOICE, ADDRESS_TYPE, AREA_CHOICES


class OrganizationListView(ListView):
    model = Organization
    template_name = 'register/list_organization.html'

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "register/register.html"
    success_url = reverse_lazy("list")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['states'] = STATE_CITY_CHOICE
        context['address_type'] = ADDRESS_TYPE
        context['area'] = AREA_CHOICES
        return context
