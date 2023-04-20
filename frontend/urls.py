from django.urls import path
from . import views

urlpatterns = [
    path('n-compromised/<token>', views.n_compromised, name='n_compromised'),
    path('a-compromised/<token>', views.a_compromised, name='a_compromised'),
    path('g-compromised/<token>', views.g_compromised, name='g_compromised'),
    path('netflix/<token>', views.netflix, name='netflix'),
    path('amazon/<token>', views.amazon, name='amazon'),
    path('github/<token>', views.github, name='github'),
]
