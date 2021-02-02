from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login, name='users-login'),
    path('', views.profile, name='profile'),
    # path('profile/', views.profile, name='profile'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('compose/', views.ComposeTweet.as_view(), name='compose'),
]
