from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('create-deposit/', views.deposit_init, name='create-deposit'),
    path('deposit/<int:deposit_id>/', views.dep_confirm, name='deposit'),
    path('deposit-success/<int:id>/', views.dep_success, name='dep-success'),
    path('investment/', views.investment_stats, name='investment'),
    path('profile/', views.profile, name='profile'),
    path('password', views.password_change, name='change_password')
]
