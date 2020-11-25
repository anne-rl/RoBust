from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from .models import *



class HeadListView(View):
    def get(self, request):
        drivers = Driver.objects.all()
        context = {
        'drivers' : drivers,
        }
        return render(request, 'head/headList.html', context)
  
    def post(self, request):
        if request.method == 'POST':
            if 'driverUpdate' in request.POST:
                print('update profile button clicked')
                Driverid = request.POST.get("driver-id")
                DriverFirstName = request.POST.get("driver-firstName")
                DriverMiddleName = request.POST.get("driver-middleName")
                DriverLastName = request.POST.get("driver-lastName")
                DriverEmailAddress = request.POST.get("driver-emailAddress")
                DriverContactNumber = request.POST.get("driver-contactNumber")
                DriverGender = request.POST.get("driver-gender")
                    
                UpdateDriver = Driver.objects.filter(id = Driverid).update(firstName = DriverFirstName, middleName = DriverMiddleName, lastName = DriverLastName, emailAddress = DriverEmailAddress, contactNumber = DriverContactNumber, gender = DriverGender)
                    
                print(UpdateDriver)
                print('Driver Updated')
            elif 'driverDelete' in request.POST:	          
                print('delete button clicked')
                Driverid = request.POST.get("deleteDriver-id")
                DeleteDriver = Driver.objects.filter(id = Driverid).delete()
                print('recorded deleted')                  
        return redirect('head:headList_view')       

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
        form = RegisterDriverForm(request.POST)
    
        if form.is_valid():
            DriverFirstName = request.POST.get("firstName")
            DriverMiddleName = request.POST.get("middleName")
            DriverLastName = request.POST.get("lastName")
            DriverEmailAddress = request.POST.get("emailAddress")
            DriverContactNumber = request.POST.get("contactNumber")
            DriverGender = request.POST.get("gender")
            BusName = request.POST.get("busName")
            BusDestination = request.POST.get("destination")
            BusPlateNumber = request.POST.get("plateNumber")
            BusSeats = request.POST.get("seats")
            BusFare = request.POST.get("busFare")
            BusTimeDeparture = request.POST.get("timeDeparture")

            form = Driver(firstName = DriverFirstName, middleName = DriverMiddleName, lastName = DriverLastName, emailAddress = DriverEmailAddress, contactNumber = DriverContactNumber, gender = DriverGender, busName = BusName, destination = BusDestination, plateNumber = BusPlateNumber, seats = BusSeats, busFare = BusFare, timeDeparture = BusTimeDeparture)
            form.save()
        
            return redirect('head:headList_view')   
        else:
            print(form.errors)
            return HttpResponse('not valid')

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