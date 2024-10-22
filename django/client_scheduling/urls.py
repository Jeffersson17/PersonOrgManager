from django.contrib import admin
from django.urls import path, include
from client_scheduling.views import HomeTemplateView
from person.views import PessoaViewSet
from rest_framework import routers
from person.views import PessoaListAPIView

router = routers.DefaultRouter()
router.register('persons', PessoaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('person/', include('person.urls')),
    path('organization/', include('organization.urls')),
    path('address/', include('address.urls')),
    path('persons/list/', PessoaListAPIView.as_view(), name='list-person'),
    path('', HomeTemplateView.as_view(), name="home"),
]

urlpatterns += router.urls
