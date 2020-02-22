from django.conf.urls import url
from parking import views

urlpatterns = [
    url(r'^parking/$', views.ParkingSerializerListView.as_view()),
]
