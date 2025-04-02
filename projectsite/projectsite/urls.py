"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studentorgs.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView
from studentorgs.views import OrgMemberList, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView
from studentorgs.views import StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView
from studentorgs.views import CollegeList, CollegeCreateView, CollegeUpdateView, CollegeDeleteView
from studentorgs.views import ProgramList, ProgramCreateView, ProgramUpdateView, ProgramDeleteView
from studentorgs import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),

    # Organization URLs
    path('organizations/', OrganizationList.as_view(), name='organization-list'),
    path('organizations/new/', OrganizationCreateView.as_view(), name='organization-create'),
    path('organizations/<int:pk>/edit/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organizations/<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),

    # OrgMember URLs
    path('orgmembers/', OrgMemberList.as_view(), name='orgmember-list'),
    path('orgmembers/new/', OrgMemberCreateView.as_view(), name='orgmember-create'),
    path('orgmembers/<int:pk>/edit/', OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmembers/<int:pk>/delete/', OrgMemberDeleteView.as_view(), name='orgmember-delete'),

    # Student URLs
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/new/', StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/edit/', StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

    # College URLs
    path('colleges/', CollegeList.as_view(), name='college-list'),
    path('colleges/new/', CollegeCreateView.as_view(), name='college-create'),
    path('colleges/<int:pk>/edit/', CollegeUpdateView.as_view(), name='college-update'),
    path('colleges/<int:pk>/delete/', CollegeDeleteView.as_view(), name='college-delete'),

    # Program URLs
    path('programs/', ProgramList.as_view(), name='program-list'),
    path('programs/new/', ProgramCreateView.as_view(), name='program-create'),
    path('programs/<int:pk>/edit/', ProgramUpdateView.as_view(), name='program-update'),
    path('programs/<int:pk>/delete/', ProgramDeleteView.as_view(), name='program-delete'),
]