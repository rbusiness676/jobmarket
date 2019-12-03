from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('agents/', views.AgentList.as_view()),
    path('agents/<int:pk>/', views.AgentDetail.as_view()),
]