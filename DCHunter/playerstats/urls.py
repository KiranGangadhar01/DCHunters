from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.home, name='playerlist'),
    path('add/', views.stats, name='inputstats'),
    path('totalwins/', views.wins, name='totalwins'),
    path('totalmatches/', views.match, name='totalmatches'),
    path('totalkills/', views.kills, name='totalkills'),
    path('headshot/', views.headshot, name='totalheadshot'),
    path('mostkills/', views.mostkills, name='mostkills'),
    path('topseason05/', views.topseason05, name='topseason05'),
]
