from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path("admins", views.admins, name='admins'),

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout_view, name='logout')
]
