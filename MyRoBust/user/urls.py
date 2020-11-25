from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'user'

urlpatterns = [
	path('landing', views.LandingIndexView.as_view(), name="landing_view"),
    path('userReservation', views.UserReservationView.as_view(), name="userReservation_view"),
    path('userSelect', views.UserSelectView.as_view(), name="userSelect_view"),
    path('userSelectUpdate', views.UserSelectUpdateView.as_view(), name="userSelectUpdate_view"),
    path('userReview', views.UserReviewView.as_view(), name="userReview_view"),
    path('userDashboardWeekly', views.UserDashboardViewWeekly.as_view(), name="userDashboard_weekly"),
    path('userDashboardMonthly', views.UserDashboardViewMonthly.as_view(), name="userDashboard_monthly")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)