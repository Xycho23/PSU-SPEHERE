from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from studentorgs.models import Organization, OrgMember, Student, College, Program
from studentorgs.forms import OrganizationForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

# Organization Views
@method_decorator(login_required, name='dispatch')
class OrganizationList(ListView):
    model = Organization
    template_name = 'organization_list.html'
    context_object_name = 'organization'  # Changed from 'organizations' to 'organization'
    paginate_by = 10
    
    def get_queryset(self):
        return Organization.objects.all().order_by('id')  # Add default ordering

@method_decorator(login_required, name='dispatch')
class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

@method_decorator(login_required, name='dispatch')
class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

@method_decorator(login_required, name='dispatch')
class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

# OrgMember Views
@method_decorator(login_required, name='dispatch')
class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'orgmember_list.html'
    paginate_by = 5

@method_decorator(login_required, name='dispatch')
class OrgMemberCreateView(CreateView):
    model = OrgMember
    fields = '__all__'
    template_name = 'orgmember_add.html'
    success_url = reverse_lazy('orgmember-list')

@method_decorator(login_required, name='dispatch')
class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    fields = '__all__'
    template_name = 'orgmember_edit.html'
    success_url = reverse_lazy('orgmember-list')

@method_decorator(login_required, name='dispatch')
class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')

# Student Views
@method_decorator(login_required, name='dispatch')
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'student_list.html'
    paginate_by = 5

@method_decorator(login_required, name='dispatch')
class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')

@method_decorator(login_required, name='dispatch')
class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'student_edit.html'
    success_url = reverse_lazy('student-list')

@method_decorator(login_required, name='dispatch')
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

# College Views
@method_decorator(login_required, name='dispatch')
class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'college_list.html'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(Q(college_name__icontains=query))
        return qs

@method_decorator(login_required, name='dispatch')
class CollegeCreateView(CreateView):
    model = College
    fields = '__all__'
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')

@method_decorator(login_required, name='dispatch')
class CollegeUpdateView(UpdateView):
    model = College
    fields = '__all__'
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')

@method_decorator(login_required, name='dispatch')
class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

# Program Views
@method_decorator(login_required, name='dispatch')
class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'program_list.html'
    paginate_by = 5

@method_decorator(login_required, name='dispatch')
class ProgramCreateView(CreateView):
    model = Program
    fields = '__all__'
    template_name = 'program_add.html'
    success_url = reverse_lazy('program-list')

@method_decorator(login_required, name='dispatch')
class ProgramUpdateView(UpdateView):
    model = Program
    fields = '__all__'
    template_name = 'program_edit.html'
    success_url = reverse_lazy('program-list')

@method_decorator(login_required, name='dispatch')
class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')

# Search View
@login_required
def search_view(request):
    try:
        query = request.GET.get('q', '')
        if query:
            students = Student.objects.filter(
                Q(student_id__icontains=query) |
                Q(firstname__icontains=query) |
                Q(lastname__icontains=query)
            )
            organizations = Organization.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
            colleges = College.objects.filter(college_name__icontains=query)
        else:
            students = Student.objects.none()
            organizations = Organization.objects.none()
            colleges = College.objects.none()

        context = {
            'query': query,
            'students': students,
            'organizations': organizations,
            'colleges': colleges,
        }
        return render(request, 'search_results.html', context)
    except Exception as e:
        print(f"Search error: {str(e)}")
        return render(request, 'search_results.html', {
            'query': query,
            'error': 'An error occurred during search'
        })