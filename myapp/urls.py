from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.home_page,name='home_page')
]
