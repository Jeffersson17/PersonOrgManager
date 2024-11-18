from django.contrib import admin
from django.urls import path, include
from client_scheduling.views import HomeTemplateView
from person.views import PessoaViewSet
from organization.views import OrganizationViewSet
from rest_framework import routers
from person.views import PessoaListAPIView, PessoaCreateAPIView, PessoaDetailAPIView
from organization.views import OrganizationDetailAPIView, OrganizationListAPIView, StatusChoices
from address.views import AddressViewSet, CityViewSet

router = routers.DefaultRouter()
router.register('persons', PessoaViewSet)
router.register('organizations', OrganizationViewSet)
router.register('address', AddressViewSet)
router.register('city', CityViewSet)

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('person/', include('person.urls')),
    path('organization/', include('organization.urls')),
    path('address/', include('address.urls')),
    path('persons/list-api/', PessoaListAPIView.as_view(), name='list-person-api'),
    path('persons/create-api/', PessoaCreateAPIView.as_view(), name='create-person-api'),
    path('persons/detail-api/<int:pk>/', PessoaDetailAPIView.as_view(), name='detail-person-api'),
    path('organizations/detail-api/<int:pk>/', OrganizationDetailAPIView.as_view(), name='detail-organization-api'),
    path("organization/list-api/", OrganizationListAPIView.as_view(), name='organization-list-api'),
    path('api/choices/', StatusChoices.as_view(), name='organization-choices-api')
]
