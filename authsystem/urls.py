from django.urls import path
from authsystem import views


app_name = 'authsystem'
urlpatterns = [
  
     # path('login/',views.logview),
     # path('register/',views.regview),
     path('myregister/',views.register_user,name='myregister'),
     path('login_user/',views.login_user,name='login'),
     path('logout_user/',views.logout_user,name='logout'),
]