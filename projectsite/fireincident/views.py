from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Locations, Incident, FireStation

class HomePageView(TemplateView):
    template_name = 'home.html'

class ChartView(TemplateView):
    template_name = 'chart.html'  # Update this line to use chart.html

class PieCountbySeverity(TemplateView):
    template_name = 'pie_severity.html'

class LineCountbyMonth(TemplateView):
    template_name = 'line_month.html'

class MultilineIncidentTop3Country(TemplateView):
    template_name = 'multiline_top3.html'

def multipleBarbySeverity(request):
    return render(request, 'multiple_bar.html')  # Template will now be found in global templates directory

def map_station(request):
    return render(request, 'map.html')
