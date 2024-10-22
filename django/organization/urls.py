from django.urls import path
from organization.views import OrganizationCreateView,OrganizationListView, OrganizationUpdateView, OrganizationDeleteView

urlpatterns = [
    path('list_organization/', OrganizationListView.as_view(), name="list_organization"),
    path('register/', OrganizationCreateView.as_view(), name="register_organization"),
    path('update/<int:pk>/', OrganizationUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', OrganizationDeleteView.as_view(), name="delete"),
]