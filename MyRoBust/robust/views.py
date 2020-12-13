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
# from django.contrib.auth import update_session_auth_hash

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
                    
                elif 'userUpdateBtn' in request.POST:
                    print('update profile button clicked')
                    UserId = request.POST.get("user-id")
                    UserFirstName = request.POST.get("user-firstName")
                    UserLastName = request.POST.get("user-lastName")
                    UserUsername = request.POST.get("user-username")
                    UserEmailAddress = request.POST.get("user-emailAddress")

                    UpdateUser = User.objects.filter(id = UserId).update(first_name = UserFirstName, last_name = UserLastName, username = UserUsername, email = UserEmailAddress)

                    print(UpdateUser)
                    print('User Updated')
                    
                elif 'adminUpdateBtn' in request.POST:
                    print('update profile button clicked')
                    AdminId = request.POST.get("user-id")
                    AdminFirstName = request.POST.get("admin-firstName")
                    AdminLastName = request.POST.get("admin-lastName")
                    AdminUsername = request.POST.get("admin-username")
                    AdminEmailAddress = request.POST.get("user-emailAddress")

                    UpdateAdmin = User.objects.filter(id = UserId).update(first_name = AdminFirstName, last_name = AdminLastName, username = AdminUsername, email = AdminEmailAddress)

                    print(UpdateAdmin)
                    print('User Updated')
                    
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
                
                #For EWallet where the name of DB is Profile
                form = EWalletForm(request.POST)
                user = request.user
                                                                               
                availableBalance = request.POST.get("availableBalance")
                currentCashIn = request.POST.get("currentCashIn")
                form = EWallet(id = user, availableBalance = availableBalance , currentCashIn = currentCashIn)
                form.save()
        
                #Count all the users 
                form = DashboardUserForm(request.POST)
                user=request.user
                allUsers = User.objects.count()   
                form = DashboardUser(totalUsers = allUsers, userLogIn = user)
                form.save()
                
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

        def post(self,request):  
            id = request.POST.get('busID')
            date_reserved = request.POST.get('dateReservation')
            global getID
            global getdBooked
            def getID():
                return id;
            def getdBooked():
                return date_reserved;
            return redirect('robust:userSelect_view')
    
class UserSelectView(View):
        # model = Bus
        def get(self,request):
            id = getID()
            dBooked = getdBooked()
            bus = Bus.objects.get(busID=id)
            qs_booking = Bus.objects.filter(busID=id)  
            context = {
                'bookings': qs_booking,
                'Booked' : dBooked
            }
            return render(request, 'user/userSelect.html', context)

        def post(self, request):
            form = BookingForm(request.POST or None)    
            if request.method == 'POST':
                if form.is_valid():
                    user=request.user
                    dBooked = request.POST.get("dateReservation")
                    t_object1 = datetime.datetime.strptime(dBooked, " %Y-%m-%d")
                    t_object2 = datetime.datetime.strftime(t_object1,"%Y-%m-%d")
                    seatNumber = request.POST.get("seatNumber")
                    bus = request.POST['busID']
                    form = Booking(dateReservation=t_object2, seatNumber = seatNumber, bus_id=bus, user = user)
                    form.save()
                        
                    return redirect('robust:userReview_view')       
            
                else:
                    print(form.errors)
                    return HttpResponse('not valid')
            
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
            booking_id = request.POST.get("booking_id")
            dateReservation = request.POST.get("booking-date_booked")
            global getBookingID
            global getBookingDate
            def getBookingID():
                return booking_id
            def getBookingDate():
                return dateReservation;    

            return redirect('robust:userSelectUpdate_view')
          
class UserSelectUpdateView(View):
        def get(self, request):
            booking_id = getBookingID()
            dateReservation = getBookingDate()
            qs_booking = Booking.objects.get(booking = booking_id)
            busID = qs_booking.bus_id
            qs_bus = Bus.objects.get(busID = busID)
            context = {
               'booking_id' : booking_id,
               'bus' : qs_bus,
               'dateReservation' : dateReservation
            }
            return render(request, 'user/userSelectUpdate.html',context)

        def post(self, request):
            if request.method == 'POST':
                    booking_id = request.POST.get('booking_id')
                    dateReservation = request.POST.get('dateReservation')
                    t_object1 = datetime.datetime.strptime(dateReservation, " %Y-%m-%d")
                    t_object2 = datetime.datetime.strftime(t_object1,"%Y-%m-%d")
                    seatNumber = request.POST.get('seatNumber')
                    UpdateBooking = Booking.objects.filter(booking = booking_id).update(seatNumber = seatNumber, dateReservation = t_object2)
                    print(UpdateBooking)
            return redirect('robust:userReview_view')
                

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
        user = User.objects.all()
        ewallet = EWallet.objects.all()
        context = {
            'users' : user,
            'ewallets' : ewallet
        }
        return render(request, 'admin/adminList.html', context)
        #return render(request, 'admin/adminList.html',{'users':users, 'ewallet':ewallet})
  
    def post(self, request):
        if request.method == 'POST':
            #USER UPDATE
            if 'userUpdate' in request.POST:
                print('update profile button clicked')
                UserId = request.POST.get("user-id")
                UserFirstName = request.POST.get("user-firstName")
                UserLastName = request.POST.get("user-lastName")
                UserUsername = request.POST.get("user-username")
                UserEmailAddress = request.POST.get("user-emailAddress")
   
                UpdateUser = User.objects.filter(id = UserId).update(first_name = UserFirstName, last_name = UserLastName, username = UserUsername, email = UserEmailAddress)
                
                print(UpdateUser)
                print('User Updated')
            
            #USER DELETE
            elif 'userDelete' in request.POST:
                print('delete button clicked')
                getUserId = request.POST.get("deleteUser-username")               
                DeleteUser = User.objects.filter(id = getUserId).delete()
                print('recorded deleted')  
                
                #Delete a user to the DashboardUser 
                user=request.user
                allUsers = User.objects.count()
                form = DashboardUser(totalUsers = allUsers, userLogIn = user)
                form.save()
                
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
        allPassengers = User.objects.count()
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
        allPassengers = User.objects.count()        
        context = {
            'allBuses' : allBuses,
            'allPassengers' : allPassengers
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
        qs_drivers = Driver.objects.all()
        qs_trips = Booking.objects.all()
        context = {
            'buses' : qs_bus,
            'drivers' : qs_drivers,
            'trips' : qs_trips
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
                
                #Delete a bus to the DashboardBus 
                user=request.user
                allBuses = Bus.objects.count()
                form = DashboardBus(totalBuses = allBuses, userLogIn = user)
                form.save()
             
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
                
            #TRIP DELETE
            elif 'tripDelete' in request.POST:	          
                print('delete button clicked')
                Tripid = request.POST.get("deleteTrip-id")
                DeleteTrip = Booking.objects.filter(booking = Tripid).delete()
                print('recorded deleted') 

        return redirect('robust:adminBusTransaction_view')
       
class AdminRegisterBus(View):
    def get(self, request):
        return render(request, 'admin/adminRegisterBus.html')

    def post(self, request):

        form = BusForm(request.POST, request.FILES)

        if form.is_valid():
            user=request.user
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
            
            #Count all the buses 
            allBuses = Bus.objects.count()
            form = DashboardBus(totalBuses = allBuses, userLogIn = user)
            form.save()
            
            return redirect('robust:adminBusTransaction_view') 

        else:
            print(form.errors)
            return HttpResponse('not valid')

class AdminRegisterDriver(View):
    def get(self, request):
        return render(request, 'admin/adminRegisterDriver.html')
  
    def post(self, request):
        form = RegisterDriverForm(request.POST or None, request.FILES)
    
        if form.is_valid():
            user=request.user
            DriverProfilePicture = request.FILES.get('profilePicture')
            DriverFirstName = request.POST.get("firstName")
            DriverMiddleName = request.POST.get("middleName")
            DriverLastName = request.POST.get("lastName")
            DriverEmailAddress = request.POST.get("emailAddress")
            DriverContactNumber = request.POST.get("contactNumber")
            DriverGender = request.POST.get("gender")
    

            form = Driver(userLogIn = user, profilePicture = DriverProfilePicture, firstName = DriverFirstName, middleName = DriverMiddleName, lastName = DriverLastName, emailAddress = DriverEmailAddress, contactNumber = DriverContactNumber, gender = DriverGender)
            form.save()
        
            return redirect('robust:adminBusTransaction_view')   
        else:
            print(form.errors)
            return HttpResponse('not valid')
