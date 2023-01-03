from django.urls import path
from . import views


urlpatterns = [ 
 path('becomeinst/',views.becomeinst,
 name='becomeinst'),
 path('', views.courses, 
 name='courses'),
 path('create/',views.createcourse,
 name='createcourse'),
 path('<int:Course_ID>/',views.detail,
 name='coursedetail'),
 path('yourcourses/',views.usercourses,
 name='usercourses') ,  
]