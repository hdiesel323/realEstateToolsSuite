from django.urls import path
from django.contrib.auth import views as auth_views
from investment.views import investment_home, investment_calculator, calculate, investment_list

urlpatterns = [
    path('', investment_home, name='home'),
    path('calculator/', investment_calculator, name='investment_calculator'),
    path('calculate/', calculate, name='calculate'),
    path('investment/', investment_list, name='investment_list'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Include template
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]