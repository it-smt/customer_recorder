from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('history/', views.history, name='history'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout')
]