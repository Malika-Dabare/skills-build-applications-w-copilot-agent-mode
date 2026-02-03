from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

import os
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request, format=None):
    # Get codespace name from environment or fallback to localhost
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev"
    else:
        # fallback for local development
        base_url = "http://localhost:8000"
    return Response({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activities': f'{base_url}/api/activities/',
        'leaderboard': f'{base_url}/api/leaderboard/',
        'workouts': f'{base_url}/api/workouts/',
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
