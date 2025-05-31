from django.urls import path
from .views import (
    HomeView,
    ProgramDistributionView,
    CollegeDistributionView,
    MonthlyTrendsView,
    ChartView,  # Import the ChartView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('program-distribution/', ProgramDistributionView.as_view(), name='program_distribution'),
    path('college-distribution/', CollegeDistributionView.as_view(), name='college_distribution'),
    path('monthly-trends/', MonthlyTrendsView.as_view(), name='monthly_trends'),
    path('chart/', ChartView.as_view(), name='chart'),  # Add the URL pattern for the chart
]