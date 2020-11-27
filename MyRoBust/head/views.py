from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from .forms import *
from user.models import *


class HeadListView(View):
    def get(self, request):
        passengers = Passenger.objects.all()
        context = {
        'passengers' : passengers,
        }
        return render(request, 'head/headList.html', context)
  
    def post(self, request):
        if request.method == 'POST':
            #Passenger Update
            if 'passengerUpdate' in request.POST:
                print('update profile button clicked')
                PassengerUsername = request.POST.get("passenger-username")
                PassengerFirstName = request.POST.get("passenger-firstName")
                PassengerMiddleName = request.POST.get("passenger-middleName")
                PassengerLastName = request.POST.get("passenger-lastName")
                PassengerEmailAddress = request.POST.get("passenger-emailAddress")
                PassengerPassword = request.POST.get("passenger-password")
                PassengerDepartment = request.POST.get("passenger-department")
                PassengerContactNumber = request.POST.get("passenger-contactNumber")
                PassengerGender = request.POST.get("passenger-gender")
                
                UpdatePassenger = Passenger.objects.filter(username = PassengerUsername).update(firstName = PassengerFirstName, middleName = PassengerMiddleName, lastName = PassengerLastName, emailAddress = PassengerEmailAddress, password = PassengerPassword, department = PassengerDepartment, contactNumber = PassengerContactNumber, gender = PassengerGender)
                
                print(UpdatePassenger)
                print('Passenger Updated')
            
            #Passenger Delete
            elif 'passengerDelete' in request.POST:
                print('delete button clicked')
                getPassengerUsername = request.POST.get("deletePassenger-username")
                DeletePassenger = Passenger.objects.filter(username = getPassengerUsername).delete()
                print('recorded deleted')  
                
        return redirect('head:headList_view')       

class HeadSummaryView(View):
    def get(self, request):
        return render(request, 'head/headSummary.html')
  
    def post(self, request):
        return render(request, 'head/headSummary.html')

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

class HeadBusTransactionView(View):
    def get(self, request):
        qs_bus = Bus.objects.all()
        drivers = Driver.objects.all()
        context = {
            'buses' : qs_bus,
            'drivers' : drivers
        }
        return render(request, 'head/headBusTransaction.html', context)
  
    def post(self, request):
        if request.method == 'POST':
            #BUS UPDATE
            if 'busUpdate' in request.POST:
                bid = request.POST.get("bus-id")
                busbn = request.POST.get("bus-busName")
                buspn = request.POST.get("bus-plateNumber")
                busd = request.POST.get("bus-destination")
                busts = request.POST.get("bus-totalSeats")
                busf = request.POST.get("bus-busFare")
                busdt = request.POST.get("bus-departureTime")
                update_bus = Bus.objects.filter(id=bid).update(busName = busbn, plateNumber = buspn, 
                            destination = busd,totalSeats = busts, busFare = busf, departureTime = busdt)
                
            #BUS DELETE     
            elif 'busDelete' in request.POST:	          
                print('delete button clicked')
                bid = request.POST.get("deleteBus-id")
                delete_bus = Bus.objects.filter(id = bid).delete()
                print('recorded deleted') 
                
            #DRIVER UPDATE        
            elif 'driverUpdate' in request.POST:
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
                
            #DRIVER DELETE     
            elif 'driverDelete' in request.POST:	          
                print('delete button clicked')
                Driverid = request.POST.get("deleteDriver-id")
                DeleteDriver = Driver.objects.filter(id = Driverid).delete()
                print('recorded deleted') 

        return redirect('head:headBusTransaction_view')
       
class HeadRegisterBus(View):
    def get(self, request):
        return render(request, 'head/headRegisterBus.html')

    def post(self, request):

        form = BusForm(request.POST)

        if form.is_valid():

            bn = request.POST.get("busName")
            pn = request.POST.get("plateNumber")
            d = request.POST.get("destination")
            ts = request.POST.get("totalSeats")
            f = request.POST.get("busFare")
            dt = request.POST.get("departureTime")
            img = request.FILES.get('img')
            form = Bus(busName = bn, plateNumber = pn, destination = d,
                        totalSeats = ts, busFare = f, departureTime = dt, img = img)
            form.save()

            return redirect('head:headBusTransaction_view')

        else:
            print(form.errors)
            return HttpResponse('not valid')
class HeadRegisterDriver(View):
    def get(self, request):
        return render(request, 'head/headRegisterDriver.html')
  
    def post(self, request):
        form = RegisterDriverForm(request.POST)
    
        if form.is_valid():
            DriverFirstName = request.POST.get("firstName")
            DriverMiddleName = request.POST.get("middleName")
            DriverLastName = request.POST.get("lastName")
            DriverEmailAddress = request.POST.get("emailAddress")
            DriverContactNumber = request.POST.get("contactNumber")
            DriverGender = request.POST.get("gender")
    

            form = Driver(firstName = DriverFirstName, middleName = DriverMiddleName, lastName = DriverLastName, emailAddress = DriverEmailAddress, contactNumber = DriverContactNumber, gender = DriverGender)
            form.save()
        
            return redirect('head:headBusTransaction_view')   
        else:
            print(form.errors)
            return HttpResponse('not valid')
