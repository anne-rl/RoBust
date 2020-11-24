from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'head'

urlpatterns = [
    path('headList', views.HeadListView.as_view(), name="headList_view"),
    path('headSummary', views.HeadSummaryView.as_view(), name="headSummary_view"),
    path('headTrip', views.HeadTripView.as_view(), name="headTrip_view"),
    path('headDriverBusRegistration', views.HeadDriverBusRegistration.as_view(), name="headDriverBusRegistration_view"),
    path('headDashboardWeekly', views.HeadDashboardWeekly.as_view(), name="headDashboard_weekly"),
    path('headDashboardMonthly', views.HeadDashboardMonthly.as_view(), name="headDashboard_monthly"),
    path('headUpdateBus', views.HeadUpdateBusView.as_view(), name="headUpdateBus_view")
]