from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from .forms import PassengerForm
from head.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import *


class LandingIndexView(View):
        def get(self, request):
            return render(request, 'user/landing.html')

        def post(self, request):
            form = AdministratorForm(request.POST)
            form = PassengerForm(request.POST)

            if request.method == 'POST':
                if Admin.objects.filter(username=request.POST['username'],password=request.POST['password']).exists() : 
                    admin =Admin.objects.get(username=request.POST['username'], password=request.POST['password'])
                
                    return render(request, 'head/headList.html', {'admin': admin})

                if Passenger.objects.filter(username=request.POST['username'],password=request.POST['password']).exists() : 
                    passenger =Passenger.objects.get(username=request.POST['username'], password=request.POST['password'])
                
                    return render(request, 'user/userReservation.html', {'passenger': passenger})

                else:
#                    context = {'msg': 'Invalid username/password'}
#                    return render(request, 'user/landing.html', context)
                    print(form.errors)
                    return HttpResponse('Invalid username/password!')
            else:
                return render(request, 'user/landing.html', context)

class UserReservationView(View):
        def get(self, request):
            qs_bus = Bus.objects.all()
            context = {

                'buses' : qs_bus

            }
            return render(request, 'user/userReservation.html', context)

        def post(self, request):
            return render(request, 'user/userReservation.html')
    
class UserSelectView(View):
        def get(self, request):
            return render(request, 'user/userSelect.html')

        def post(self, request):
            return render(request, 'user/userSelect.html')
          
class UserSelectUpdateView(View):
        def get(self, request):
            return render(request, 'user/userSelectUpdate.html')

        def post(self, request):
            return render(request, 'user/userSelectUpdate.html')
                
class UserReviewView(View):
        def get(self, request):
            return render(request, 'user/userReview.html')

        def post(self, request):
            return render(request, 'user/userReview.html')

class UserDashboardViewWeekly(View):
        def get(self, request):
            return render(request, 'user/userDashboardWeekly.html')

        def post(self, request):
            return render(request, 'user/userDashboardWeekly.html')

class UserDashboardViewMonthly(View):
        def get(self, request):
            return render(request, 'user/userDashboardMonthly.html')

        def post(self, request):
            return render(request, 'user/userDashboardMonthly.html')