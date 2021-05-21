from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('news/',views.news,name="news"),
    path('applyipo/',views.applyipo,name="applyipo"),
    path('ltp/',views.ltp,name="ltp"),
    path('about/',views.about,name="about"),
    path('broker/',views.broker,name="broker")
]