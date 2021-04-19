from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('help/',views.help,name="help"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('dmatacc',views.dmatacc,name="dmatAcc")
]