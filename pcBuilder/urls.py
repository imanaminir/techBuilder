from django.urls import path
from . import views

urlpatterns = [
    path('build/', views.build_pc, name="build"),


]