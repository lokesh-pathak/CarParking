from django.urls import path

from parking import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('vehicle/', views.VehicleEntryView.as_view()),
    path('remove/$', views.vehicle_exiting, name="remove"),
]
