from django.urls import path

from researcher_app import views

urlpatterns = [
    path('', views.index, name='index'),
]