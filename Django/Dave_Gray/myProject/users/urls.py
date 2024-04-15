from django.urls import path
from . import views 

app_name = 'users'

urlpatterns = [
    path('register/'  , views.register,    name='register'),
    path('login/'     , views.login_view,  name='login'),
    path('logout/'    , views.logout_view, name='logout'),
#           URL            view_Function        view_name
#           URL can be gattered from database  <path converter: parameter> 
]

