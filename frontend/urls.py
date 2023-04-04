from django.urls import path
from . import views

urlpatterns = [
    path('adddata', views.adddata, name='adddata'),
    path('viewdb', views.viewdb, name='viewdb'),
    path('compromised/<token>', views.compromised, name='compromised'),
    path('<token>', views.index, name='index'),
]
