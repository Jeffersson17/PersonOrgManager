from django.contrib import admin
from django.urls import path, include
from client_scheduling.views import HomeTemplateView
from person.views import PessoaViewSet
from rest_framework import routers
from person.views import PessoaListAPIView, PessoaCreateAPIView

router = routers.DefaultRouter()
router.register('persons', PessoaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('person/', include('person.urls')),
    path('organization/', include('organization.urls')),
    path('address/', include('address.urls')),
    path('persons/list-api/', PessoaListAPIView.as_view(), name='list-person-api'),
    path('persons/create-api/', PessoaCreateAPIView.as_view(), name='create-person-api'),
    path('', HomeTemplateView.as_view(), name="home"),
]

urlpatterns += router.urls
