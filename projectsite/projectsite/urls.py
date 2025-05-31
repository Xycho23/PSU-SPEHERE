from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from studentorgs.views import (
    HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth,
    MultilineIncidentTop3Country, multipleBarbySeverity,
    OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView,
    OrgMemberList, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView,
    StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView,
    CollegeList, CollegeCreateView, CollegeUpdateView, CollegeDeleteView,
    ProgramList, ProgramCreateView, ProgramUpdateView, ProgramDeleteView
)
from fireincident.views import map_station

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Main URLs
    path('', HomePageView.as_view(), name='home'),

    # Authentication URLs
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Dynamic Chart Data URLs
    path('lineChart/', LineCountbyMonth.as_view(), name='lineChart'),
    path('chart/', PieCountbySeverity.as_view(), name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country.as_view(), name='multilineChart'),
    path('multiBarChart/', multipleBarbySeverity.as_view(), name='multiBarChart'),

    # Organization URLs
    path('organization_list/', OrganizationList.as_view(), name='organization-list'),
    path('organization/add/', OrganizationCreateView.as_view(), name='organization-create'),
    path('organization/<int:pk>/update/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization/<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),

    # OrgMember URLs
    path('orgmember_list', OrgMemberList.as_view(), name='orgmember-list'),
    path('orgmember_list/add', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmember_list/<pk>', OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmember_list/<pk>/delete', OrgMemberDeleteView.as_view(), name='orgmember-delete'),

    # Student URLs
    path('student_list', StudentList.as_view(), name='student-list'),
    path('student_list/add', StudentCreateView.as_view(), name='student-add'),
    path('student_list/<pk>', StudentUpdateView.as_view(), name='student-update'),
    path('student_list/<pk>/delete', StudentDeleteView.as_view(), name='student-delete'),

    # College URLs
    path('college_list', CollegeList.as_view(), name='college-list'),
    path('college_list/add', CollegeCreateView.as_view(), name='college-add'),
    path('college_list/<pk>', CollegeUpdateView.as_view(), name='college-update'),
    path('college_list/<pk>/delete', CollegeDeleteView.as_view(), name='college-delete'),

    # Program URLs
    path('program_list', ProgramList.as_view(), name='program-list'),
    path('program_list/add', ProgramCreateView.as_view(), name='program-add'),
    path('program_list/<pk>', ProgramUpdateView.as_view(), name='program-update'),
    path('program_list/<pk>/delete', ProgramDeleteView.as_view(), name='program-delete'),

    # Fire Chart URLs
    path('stations', map_station, name='map-station'),

    # Dashboard Chart URL
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
]