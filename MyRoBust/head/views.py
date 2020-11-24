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
  
class HeadDriverBusRegistration(View):
  def get(self, request):
    return render(request, 'head/headDriverBusRegistration.html')
  
  def post(self, request):
    return render(request, 'head/headDriverBusRegistration.html')
  
class HeadDashboardWeekly(View):
  def get(self, request):
    return render(request, 'head/headDashboardWeekly.html')
  
  def post(self, request):
    return render(request, 'head/headDashboardWeekly.html')

class HeadDashboardMonthly(View):
  def get(self, request):
    return render(request, 'head/headDashboardMonthly.html')
  
  def post(self, request):
    return render(request, 'head/headDashboardMonthly.html')

class HeadUpdateBusView(View):
  def get(self, request):
    return render(request, 'head/headUpdateBus.html')
  
  def post(self, request):
    return render(request, 'head/headUpdateBus.html')