from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

app_name = 'robust'

urlpatterns = [
    path('landing', views.landingIndexView, name="landing_view"),
    path('logout', views.logoutPage, name="logout_view"),
    path('userRegistration', views.UserRegistrationView, name="userRegistration_view"),
    path('userReservation', views.UserReservationView.as_view(), name="userReservation_view"),
    path('userSelect/<int:id>', views.UserSelectView.as_view(), name="userSelect_view"),
    path('userSelectUpdate', views.UserSelectUpdateView.as_view(), name="userSelectUpdate_view"),
    path('userReview', views.UserReviewView.as_view(), name="userReview_view"),
    path('userDashboardWeekly', views.UserDashboardViewWeekly.as_view(), name="userDashboard_weekly"),
    path('userDashboardMonthly', views.UserDashboardViewMonthly.as_view(), name="userDashboard_monthly"),
    path('adminList', views.AdminListView.as_view(), name="adminList_view"),
    path('adminSummary', views.AdminSummaryView.as_view(), name="adminSummary_view"),
    path('adminDashboardWeekly', views.AdminDashboardWeekly.as_view(), name="adminDashboard_weekly"),
    path('adminDashboardMonthly', views.AdminDashboardMonthly.as_view(), name="adminDashboard_monthly"),
    path('adminBusTransaction', views.AdminBusTransactionView.as_view(), name="adminBusTransaction_view"), 
    path('adminRegisterBus', views.AdminRegisterBus.as_view(), name="adminRegisterBus_view"),
    path('adminRegisterDriver', views.AdminRegisterDriver.as_view(), name="adminRegisterDriver_view")
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# (?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$'