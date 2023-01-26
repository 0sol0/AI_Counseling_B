from django.urls import path 
from articles import views

urlpatterns = [
    path('community/', views.CommunityView.as_view(), name='community_view'),
]