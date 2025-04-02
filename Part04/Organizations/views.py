from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Organizations
from .forms import OrganizationsForm

class OrganizationListView(ListView):
    model = Organizations
    template_name = 'org_list.html'

class OrganizationCreateView(CreateView):
    model = Organizations
    form_class = OrganizationsForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('org_list')

class OrganizationUpdateView(UpdateView):
    model = Organizations
    form_class = OrganizationsForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('org_list')

class OrganizationDeleteView(DeleteView):
    model = Organizations
    template_name = 'org_del.html'
    success_url = reverse_lazy('org_list')