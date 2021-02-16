from django.urls import path

from . import views
app_name = 'bookingsite'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.success, name='success')
]