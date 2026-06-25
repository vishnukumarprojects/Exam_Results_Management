from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('tenth_dash',views.tenth_dash,name='tenth_dash'),
    path('eleventh_dash',views.eleventh_dash,name='eleventh_dash'),
    path('twelveth_dash',views.twelveth_dash,name='twelveth_dash'),
    path('tenth_result',views.tenth_result,name='tenth_result'),
    path('eleventh_result',views.eleventh_result,name='eleventh_result'),
    path('twelveth_result',views.twelveth_result,name='twelveth_result'),
    path('admin_side',views.admin_side,name='admin_side')
    
    
          
                
                ]