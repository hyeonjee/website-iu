from django.urls import path
from . import views

app_name="introduction"
urlpatterns = [
    path('', views.profile, name="profile"),
    path('drama/', views.drama, name="drama"),
    path('pictures/', views.pictures, name="pictures"),
    path('music/', views.music, name="music"),
    path('album/', views.album, name="album"),
    path('cafe/', views.cafe, name="cafe"),
    path('edam/', views.edam, name="edam"),


]