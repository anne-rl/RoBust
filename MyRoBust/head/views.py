from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages



class HeadListView(View):
  def get(self, request):
    return render(request, 'head/headList.html')
  
  def post(self, request):
    return render(request, 'head/headList.html')
  
class HeadSummaryView(View):
  def get(self, request):
    return render(request, 'head/headSummary.html')
  
  def post(self, request):
    return render(request, 'head/headSummary.html')
  
class HeadTripView(View):
  def get(self, request):
    return render(request, 'head/headTrip.html')
  
  def post(self, request):
    return render(request, 'head/headTrip.html')
  
class HeadDashboardView(View):
  def get(self, request):
    return render(request, 'head/headDashboard.html')
  
  def post(self, request):
    return render(request, 'head/headDashboard.html')

class HeadUpdateBusView(View):
  def get(self, request):
    return render(request, 'head/headUpdateBus.html')
  
  def post(self, request):
    return render(request, 'head/headUpdateBus.html')