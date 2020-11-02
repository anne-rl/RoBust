from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'user'

urlpatterns = [
	path('landing', views.LandingIndexView.as_view(), name="landing_view"),
    path('userReservation', views.UserReservationView.as_view(), name="userReservation_view")
]