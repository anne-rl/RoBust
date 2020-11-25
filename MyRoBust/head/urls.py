from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'head'

urlpatterns = [
    path('headList', views.HeadListView.as_view(), name="headList_view"),
    path('headSummary', views.HeadSummaryView.as_view(), name="headSummary_view"),
    path('headDashboardWeekly', views.HeadDashboardWeekly.as_view(), name="headDashboard_weekly"),
    path('headDashboardMonthly', views.HeadDashboardMonthly.as_view(), name="headDashboard_monthly"),
    path('headBusTransaction', views.HeadBusTransactionView.as_view(), name="headBusTransaction_view"), 
    path('headRegisterBus', views.HeadRegisterBus.as_view(), name="headRegisterBus_view"),
    path('headRegisterDriver', views.HeadRegisterDriver.as_view(), name="headRegisterDriver_view"),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)