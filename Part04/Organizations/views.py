from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from studentorg.models import Organizations
from studentorg.forms import OrganizationForm
from django.urls import reverse_lazy
from .models import Organizations
paginate_by = 5

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')
