from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('p', views.p),
    path('p/p1', views.p1),
    path('p/L1', views.L1, name='L1'),
    #path('p/L2', views.L2, name='L2')
    path('p/L3', views.L3, name='L3'),
    path('p/L4', views.L4, name='L4'),
    path('p/p2', views.p2),
    path('p/p3', views.p3),
    path('p/p4', views.p4),
    path('p/p5', views.p5),
    path('p/p6', views.p6),
    path('p/p7', views.p7),
    path('p/p8', views.p8),
    path('p/p9', views.p9),
]
