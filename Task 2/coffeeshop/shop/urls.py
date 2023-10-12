from django.urls import path

from . import views

urlpatterns = [
        path("",views.index,name="index"), path('save/', views.save_text, name='save_text'),path("login.html/",views.index,name="login") ]
