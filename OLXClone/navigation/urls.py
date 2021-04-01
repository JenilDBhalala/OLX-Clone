from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="OLXClone"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path("search/", views.search, name="Search"),
]