from django.urls import path
from . import forms
from . import views
urlpatterns = [
 path('signup/', views.signup,
 name='signup'),
 path('logout/', views.logoutaccount,
 name='logoutaccount'),
 path('login/', views.loginaccount,
 name='loginaccount'),
 path('profile/',views.profile,
 name='profile'),
 path('testomonial/',views.testimonial,
name='testomonial'),
path('buyprice/<int:Price_ID>',views.buyprice,
name='buyprice')
]