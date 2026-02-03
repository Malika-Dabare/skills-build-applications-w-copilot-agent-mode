from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activities': '/api/activities/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('', api_root, name='api-root'),
        path('users/', views.UserListView.as_view(), name='user-list'),
        path('teams/', views.TeamListView.as_view(), name='team-list'),
        path('activities/', views.ActivityListView.as_view(), name='activity-list'),
        path('leaderboard/', views.LeaderboardView.as_view(), name='leaderboard'),
        path('workouts/', views.WorkoutListView.as_view(), name='workout-list'),
    ])),
    path('', api_root),
]
