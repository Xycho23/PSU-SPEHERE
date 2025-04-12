from django.urls import path
from .views import OrganizationListView, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView

urlpatterns = [
    path('', OrganizationListView.as_view(), name='org_list'),  # For /organizations/
    path('add/', OrganizationCreateView.as_view(), name='org_add'),  # For /organizations/add/
    path('<int:pk>/edit/', OrganizationUpdateView.as_view(), name='org_edit'),  # For /organizations/<id>/edit/
    path('<int:pk>/delete/', OrganizationDeleteView.as_view(), name='org_delete'),  # For /organizations/<id>/delete/
]