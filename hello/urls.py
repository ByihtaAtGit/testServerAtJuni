from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='hello_index'),
	path('hello/', views.myView, name='myView'),
	path('db/', views.db, name='db'),
	]