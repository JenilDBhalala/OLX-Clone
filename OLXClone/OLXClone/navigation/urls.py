from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="OLXClone"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("help/", views.help, name="Help"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    # path("search/", views.search, name="Search"),
    # path("productview/", views.productview, name="ProductView"),
    # path("checkout/", views.checkout, name="CheckOut"),
    # path("", views.index, name="OLXClone")
    # path("", views.index, name="OLXClone")
]