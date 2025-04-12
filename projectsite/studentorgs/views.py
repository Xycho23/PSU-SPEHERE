from django.shortcuts import render

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from studentorgs.models import Organization, OrgMember, Student, College, Program
from studentorgs.forms import OrganizationForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth

from django.db models import Count
from datetime import datetime

@method_decorator(login_required, name='dispatch')
# Home Page View
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

class ChartView(ListView);
    template_name = 'chart.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context

    def get queryset(self, *args, **kwargs):
        pass

def PieCountbySeverity(request):
    query = ' ' '
    SELECT severity_level, COUNT(*) as count
    FROM fire incident
    GROUP BY severity_level
    ' ' '
    data = {}
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        
    if rows:
        data = {severity: count for severity, count in rows}
    else:
        data = {}
    return JsonResponse(data)
    
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q

# Organization Views
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'organization_list.html'
    paginate_by = 5


class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

# OrgMember Views
class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'orgmember_list.html'
    paginate_by = 5


class OrgMemberCreateView(CreateView):
    model = OrgMember
    fields = '__all__'
    template_name = 'orgmember_add.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    fields = '__all__'
    template_name = 'orgmember_edit.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')

# Student Views
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'student_list.html'
    paginate_by = 5


class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

# College Views
class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'college_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(CollegeList, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") is not None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(college_name__icontains=query))
        return qs

class CollegeCreateView(CreateView):
    model = College
    fields = '__all__'
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    fields = '__all__'
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

# Program Views
class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'program_list.html'
    paginate_by = 5


class ProgramCreateView(CreateView):
    model = Program
    fields = '__all__'
    template_name = 'program_add.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    fields = '__all__'
    template_name = 'program_edit.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')