from django.urls import path

from Hostel_Management_App import views

urlpatterns = [
   path('new',views.new,name='new'),
   path('base',views.base,name='base'),
   # path('register',views.registerPage,name='register')

]
