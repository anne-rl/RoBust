from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages


class LandingIndexView(View):
  def get(self, request):
    return render(request, 'user/landing.html')
  
  def post(self, request):
    return render(request, 'user/landing.html')
  
class UserReservationView(View):
  def get(self, request):
    return render(request, 'user/userReservation.html')
  
  def post(self, request):
    return render(request, 'user/userReservation.html')
  
class UserReviewView(View):
  def get(self, request):
    return render(request, 'user/userReview.html')
  
  def post(self, request):
    return render(request, 'user/userReview.html')
  
class UserDashboardView(View):
  def get(self, request):
    return render(request, 'user/userDashboard.html')
  
  def post(self, request):
    return render(request, 'user/userDashboard.html')