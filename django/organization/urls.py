from django.urls import path
from organization.views import OrganizationCreateView,OrganizationListView

urlpatterns = [
    path('list_organization', OrganizationListView.as_view(), name="list_organization"),
    path('register', OrganizationCreateView.as_view(), name="register"),
]