from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from studentorgs.models import Organization, OrgMember, Student, College, Program
from studentorgs.forms import OrganizationForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Q
from django.db.models.functions import ExtractMonth
from django.db.models import Count
from typing import Any
from fireincident.models import Locations, Incident, FireStation, FireIncident
from django.views import View

class ChartView(ListView):
    template_name = 'chart.html'
    model = FireIncident

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Severity data for pie chart
        severity_counts = FireIncident.objects.values('severity_level').annotate(count=Count('id'))
        context['severity_data'] = {item['severity_level']: item['count'] for item in severity_counts}
        
        # Monthly data for line chart
        current_year = datetime.now().year
        monthly_counts = FireIncident.objects.filter(date__year=current_year) \
            .annotate(month=ExtractMonth('date')) \
            .values('month') \
            .annotate(count=Count('id')) \
            .order_by('month')
        
        months = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun',
                 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
        context['monthly_data'] = {months[item['month']]: item['count'] 
                                 for item in monthly_counts}

        return context

@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

class PieCountbySeverity(TemplateView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        severity_counts = FireIncident.objects.values('severity_level').annotate(count=Count('id'))
        context['severity_data'] = {item['severity_level']: item['count'] for item in severity_counts}
        return context

class LineCountbyMonth(View):
    def get(self, request, *args, **kwargs):
        current_year = datetime.now().year
        result = {month: 0 for month in range(1, 13)}
        incidents_per_month = Incident.objects.filter(date_time__year=current_year) \
            .annotate(month=ExtractMonth('date_time')) \
            .values('month') \
            .annotate(count=Count('id'))

        for entry in incidents_per_month:
            result[entry['month']] = entry['count']

        month_names = {
            1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
            7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
        }
        result_with_month_names = {month_names[month]: count for month, count in result.items()}
        return JsonResponse(result_with_month_names)

class MultilineIncidentTop3Country(View):
    def get(self, request, *args, **kwargs):
        query = '''
        SELECT
            c.college_name as location,
            strftime('%m', so.created_at) AS month,
            COUNT(so.id) AS org_count
        FROM
            studentorgs_organization so
        JOIN
            studentorgs_college c ON so.college_id = c.id
        WHERE
            c.college_name IN (
                SELECT
                    c2.college_name
                FROM
                    studentorgs_organization so2
                JOIN
                    studentorgs_college c2 ON so2.college_id = c2.id
                WHERE
                    strftime('%Y', so2.created_at) = strftime('%Y', 'now')
                GROUP BY
                    c2.college_name
                ORDER BY
                    COUNT(so2.id) DESC
                LIMIT 3
            )
            AND strftime('%Y', so.created_at) = strftime('%Y', 'now')
        GROUP BY
            c.college_name, month
        ORDER BY
            c.college_name, month;
        '''
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        result = {}
        months = set(str(i).zfill(2) for i in range(1, 13))

        for row in rows:
            country = row[0]
            month = row[1]
            total_incidents = row[2]
            if country not in result:
                result[country] = {month: 0 for month in months}
            result[country][month] = total_incidents

        while len(result) < 3:
            missing_country = f"Country {len(result) + 1}"
            result[missing_country] = {month: 0 for month in months}

        for country in result:
            result[country] = dict(sorted(result[country].items()))

        return JsonResponse(result)

class multipleBarbySeverity(View):
    def get(self, request, *args, **kwargs):
        query = '''
        SELECT
            so.severity_level,
            strftime('%m', so.created_at) AS month,
            COUNT(so.id) AS incident_count
        FROM
            studentorgs_organization so
        GROUP BY
            so.severity_level, month
        '''
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        result = {}
        months = set(str(i).zfill(2) for i in range(1, 13))

        for row in rows:
            level = str(row[0])
            month = row[1]
            total_incidents = row[2]
            if level not in result:
                result[level] = {month: 0 for month in months}
            result[level][month] = total_incidents

        for level in result:
            result[level] = dict(sorted(result[level].items()))

        return JsonResponse(result)

def map_station(request):
    fireStations = FireStation.objects.values('name', 'latitude', 'longitude')

    for fs in fireStations:
        fs['latitude'] = float(fs['latitude'])
        fs['longitude'] = float(fs['longitude'])

    fireStations_list = list(fireStations)

    context = {
        'fireStations': fireStations_list,
    }

    return render(request, 'map_station.html', context)

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

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
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