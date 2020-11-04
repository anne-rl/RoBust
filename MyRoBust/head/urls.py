from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'head'

urlpatterns = [
    path('headHistory', views.HeadHistoryView.as_view(), name="headHistory_view"),
    path('headSummary', views.HeadSummaryView.as_view(), name="headSummary_view"),
    path('headDashboard', views.HeadDashboardView.as_view(), name="headDashboard_view")
]