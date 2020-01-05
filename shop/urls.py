from django.urls import path
from . import views 

app_name='shop'

urlpatterns=[
path('',views.landing,name='landing'),
path('<int:cat_id>/landing',views.landing,name='landing'),
path('<int:pid>/descreption/',views.descrpetion,name='descreption'),
]