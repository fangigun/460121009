from django.urls import path
from . import views

urlpatterns = [ 
 path('',views.blogs,
 name='blogs'),   
 path('<int:Blog_ID>', views.detail, 
 name='detail'),
 path('create/', views.createblog, 
 name='createblog')
]

