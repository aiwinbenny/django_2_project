from django.conf.urls import url
from app import views

urlpatterns =[
    url(r'^$',views.fun,name = 'aiwin'),
    # url(r'^page/',views.fun2,name = 'hello'),

]
