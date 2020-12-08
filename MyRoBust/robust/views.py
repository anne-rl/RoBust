from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.http import Http404
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
import datetime
from django.core.paginator import Paginator, EmptyPage
from itertools import chain
from django.http import HttpResponseRedirect
from django.urls import reverse

def landingIndexView(request):
        if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request,user)
                    request.session['username'] = username

                    if request.user.is_superuser:
                        return redirect('robust:adminList_view')   
                    else:
                        return redirect('robust:userReservation_view')
                else:
#                    messages.info(request, 'Incorrect username/password')
                    context = {'msg': 'Invalid username/password'}
                    return render(request, 'user/landing.html', context)
    
        context = {}
        return render(request, 'user/landing.html', context)
    
def logoutPage(request):
        logout(request)
        return redirect('robust:landing_view')

def UserRegistrationView(request):
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(data=request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for'+user)
                return redirect('robust:adminList_view')
        
        context = {'form' : form}
        return render(request,'user/userRegistration.html', context)
   
    
#class LandingIndexView(View):
#        def get(self, request):
#            return render(request, 'user/landing.html')
#
#        def post(self, request):
#            form = AdministratorForm(request.POST)
#            form = PassengerForm(request.POST)
#
#            if request.method == 'POST':
#                if Admin.objects.filter(username=request.POST['username'],password=request.POST['password']).exists() : 
#                    admin = Admin.objects.get(username=request.POST['username'], password=request.POST['password'])
#                
#                    return render(request, 'admin/adminList.html', {'admin': admin})
##                    return redirect('robust:adminList_view')   
#
#                if Passenger.objects.filter(username=request.POST['username'],           password=request.POST['password']).exists() : 
#                    passenger = Passenger.objects.get(username=request.POST['username'], password=request.POST['password'])
#                
#                    return render(request, 'user/userReservation.html', {'passenger': passenger})
##                    return redirect('robust:userReservation_view')   
#
#                else:
#                    context = {'msg': 'Invalid username/password'}
#                    return render(request, 'user/landing.html', context)
##                    print(form.errors)
##                    return HttpResponse('Invalid username/password!')
#            else:
#                return render(request, 'user/landing.html', context)

class UserReservationView(View):
        def get(self, request):
            qs_bus = Bus.objects.all()
            context = {
                'buses' : qs_bus
            }
            return render(request, 'user/userReservation.html', context)

        def post(self, request):
            return render(request, 'user/userReservation.html')

# def UserSelect(request, id):
#     bus = Bus.objects.get(bus=id)
#     qs_booking = Booking.objects.filter(bus=id)
#     context = {
#         'bookings': qs_booking
#     }
#     return render(request, 'user/userSelect.html', context)
    
class UserSelectView(View):
        # model = Bus
        def get(self,request,id, month, day, year):
            bus = Bus.objects.get(busID=id)
            qs_booking = Bus.objects.filter(busID=id)  
            context = {
                'bookings': qs_booking
            }
            return render(request, 'user/userSelect.html', context)

        def post(self, request, id):
            form = BookingForm(request.POST)    

            if form.is_valid():
                dBooked = request.POST.get("dateBooked")   
                seatNumber = request.POST.get("seatNumber")
                bus = request.POST['busID']
                form = Booking(date_booked=dBooked, seatNumber = seatNumber, bus_id=bus)
                form.save()
                
                return redirect('robust:userReview_view')       
    
            else:
                print(form.errors)
                return HttpResponse('not valid')
            
            
class UserSelectUpdateView(View):
        def get(self, request):
            return render(request, 'user/userSelectUpdate.html')

        def post(self, request):
            return render(request, 'user/userSelectUpdate.html')
                
class UserReviewView(View):
        def get(self,request):   
            booking = Booking.objects.all()
            bus = Bus.objects.all()
            context = {
                'buses': bus,
                'bookings': booking
            }
            return render(request, 'user/userReview.html', context)

        def post(self, request):
            if request.method == 'POST':
#                if 'seatsUpdateBtn' in request.POST:
#                    print('update booking button clicked')
               dBooked = request.POST.get("booking-date_booked")
               bName = request.POST.get("bus-busName")
               pNumber = request.POST.get("bus-plateNumber")
               pdestination = request.POST.get("bus-destination")
               tDeparture = request.POST.get("bus-timeDeparture")
               tNumber = request.POST.get("booking-ticketNumber")
               dReservation = request.POST.get("booking-dateReservation")
                                                                                              
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
          
          
          
class AdminListView(View):
    def get(self, request):
        passengers = Passenger.objects.all()
        context = {
            'passengers' : passengers,
        }
        return render(request, 'admin/adminList.html', context)
  
    def post(self, request):
        if request.method == 'POST':
            #PASSENGER UPDATE
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
            
            #PASSENGER DELETE
            elif 'passengerDelete' in request.POST:
                print('delete button clicked')
                getPassengerUsername = request.POST.get("deletePassenger-username")
                DeletePassenger = Passenger.objects.filter(username = getPassengerUsername).delete()
                print('recorded deleted')  
                
            #PASSENGER CASH IN
            elif 'passengerCashIn' in request.POST:
                getPassengerUsername = request.POST.get("cashInPassenger-username") 
                CashInUpdate = request.POST.get("cashIn-amount")
                AvailableBalance = request.POST.get("available-balance")
               
                if (AvailableBalance == 0) : 
                    AvailableBalanceUpdate = (int(AvailableBalance)-int(CashInUpdate))
                else :
                    AvailableBalanceUpdate = (int(AvailableBalance)+int(CashInUpdate))
                
                UpdatePassengerCashIn = Passenger.objects.filter(username = getPassengerUsername).update(availableBalance = AvailableBalanceUpdate, currentCashIn = CashInUpdate)
                print(UpdatePassengerCashIn)
                
        return redirect('robust:adminList_view')   
        #return render(request, 'admin/adminList.html')           

class AdminSummaryView(View):
    def get(self, request):
        booking = Booking.objects.all()
        bus = Bus.objects.all()
        context = {
            'buses': bus,
            'bookings': booking
        }
        return render(request, 'admin/adminSummary.html', context)
  
    def post(self, request):
        return render(request, 'admin/adminSummary.html')

class AdminDashboardWeekly(View):
    def get(self, request):
        allBuses = Bus.objects.count()
        allPassengers = Passenger.objects.count()
        context = {
            'allBuses' : allBuses, 
            'allPassengers' : allPassengers
        }
        return render(request, 'admin/adminDashboardWeekly.html', context)
  
    def post(self, request):
        return render(request, 'admin/adminDashboardWeekly.html')

class AdminDashboardMonthly(View):
    def get(self, request):
        allBuses = Bus.objects.count()
                
        context = {
            'allBuses' : allBuses
        }
        return render(request, 'admin/adminDashboardMonthly.html', context)
  
    def post(self, request):
#        form = AdminDashboardMonthlyForm(request.POST)
#        
#        if form.is_valid():  
#            monthlyTotalBus = request.POST.get("allBuses")
#            
#            form = DashboardAdmin(totalBuses = monthlyTotalBus)
#            form.save()
#            
#            print('hello')
            
            return redirect('robust:adminDashboard_monthly')
        
#        else:
#            print(form.errors)
#            return HttpResponse('not valid')

class AdminBusTransactionView(View):
    def get(self, request):
        qs_bus = Bus.objects.all()
        drivers = Driver.objects.all()
        context = {
            'buses' : qs_bus,
            'drivers' : drivers
        }
        return render(request, 'admin/adminBusTransaction.html', context)
  
    def post(self, request):
        if request.method == 'POST':
            #BUS UPDATE
            if 'busUpdate' in request.POST:
                bid = request.POST.get("bus-id")
                busBName = request.POST.get("bus-busName")
                busPNumber = request.POST.get("bus-plateNumber")
                busDes = request.POST.get("bus-destination")
                busSeats = request.POST.get("bus-totalSeats")
                busBsFare = request.POST.get("bus-busFare")
                busDTime = request.POST.get("bus-departureTime")
                UpdateBus = Bus.objects.filter(busID=bid).update(busName = busBName, plateNumber = busPNumber, 
                            destination = busDes, totalSeats = busSeats, busFare = busBsFare, departureTime = busDTime)
                
            #BUS DELETE     
            elif 'busDelete' in request.POST:	          
                print('delete button clicked')
                bid = request.POST.get("deleteBus-id")
                deleteBus = Bus.objects.filter(busID = bid).delete()
                print('recorded deleted') 
                
            #DRIVER UPDATE        
            elif 'driverUpdate' in request.POST:
                print('update profile button clicked')
                Driverid = request.POST.get("driver-id")
                DriverProfilePicture = request.POST.get("driver-profilePicture")
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

        return redirect('robust:adminBusTransaction_view')
       
class AdminRegisterBus(View):
    def get(self, request):
        return render(request, 'admin/adminRegisterBus.html')

    def post(self, request):

        form = BusForm(request.POST, request.FILES)

        if form.is_valid():

            busBName = request.POST.get("busName")
            busPNumber = request.POST.get("plateNumber")
            busDes = request.POST.get("destination")
            busSeats = request.POST.get("totalSeats")
            busBsFare = request.POST.get("busFare")
            busDTime = request.POST.get("departureTime")
            img = request.FILES.get('img')
            form = Bus(busName = busBName, plateNumber = busPNumber, destination = busDes,
                        totalSeats = busSeats, busFare = busBsFare, departureTime = busDTime, img = img)
            form.save()
            
            allBuses = Bus.objects.count()
        
            form = DashboardBus(totalBuses = allBuses)
            form.save()

            return redirect('robust:adminBusTransaction_view')

        else:
            print(form.errors)
            return HttpResponse('not valid')

class AdminRegisterDriver(View):
    def get(self, request):
        return render(request, 'admin/adminRegisterDriver.html')
  
    def post(self, request):
        form = RegisterDriverForm(request.POST, request.FILES)
    
        if form.is_valid():
            DriverProfilePicture = request.FILES.get('profilePicture')
            DriverFirstName = request.POST.get("firstName")
            DriverMiddleName = request.POST.get("middleName")
            DriverLastName = request.POST.get("lastName")
            DriverEmailAddress = request.POST.get("emailAddress")
            DriverContactNumber = request.POST.get("contactNumber")
            DriverGender = request.POST.get("gender")
    

            form = Driver(profilePicture = DriverProfilePicture, firstName = DriverFirstName, middleName = DriverMiddleName, lastName = DriverLastName, emailAddress = DriverEmailAddress, contactNumber = DriverContactNumber, gender = DriverGender)
            form.save()
        
            return redirect('robust:adminBusTransaction_view')   
        else:
            print(form.errors)
            return HttpResponse('not valid')
