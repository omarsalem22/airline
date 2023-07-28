from django.urls import path
from . import views

app_name='flights'
urlpatterns=[

    path("index",views.index,name="index"),
    path("<int:flight_id>",views.flight,name="fligth"),
    path("<int:flight_id>/book",views.book ,name="book")

]

