from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self):
        queryset = User.objects.all()
        email = self.request.query_params.get('email', None)
        if email is not None:
            queryset = queryset.filter(email=email)
        return queryset


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        team = self.get_object()
        users = User.objects.filter(team=team.name)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    
    def get_queryset(self):
        queryset = Activity.objects.all()
        user_email = self.request.query_params.get('user_email', None)
        if user_email is not None:
            queryset = queryset.filter(user_email=user_email)
        return queryset.order_by('-date')
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Update user's total points
        user_email = serializer.validated_data['user_email']
        points = serializer.validated_data['points']
        try:
            user = User.objects.get(email=user_email)
            user.total_points += points
            user.save()
            
            # Update team's total points
            team = Team.objects.get(name=user.team)
            team.total_points += points
            team.save()
        except (User.DoesNotExist, Team.DoesNotExist):
            pass
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    
    def get_queryset(self):
        return Leaderboard.objects.all().order_by('rank')
    
    @action(detail=False, methods=['post'])
    def update_leaderboard(self, request):
        # Clear existing leaderboard
        Leaderboard.objects.all().delete()
        
        # Get all users sorted by total points
        users = User.objects.all().order_by('-total_points')
        
        # Create new leaderboard entries
        for rank, user in enumerate(users, start=1):
            Leaderboard.objects.create(
                user_email=user.email,
                user_name=user.name,
                team=user.team,
                total_points=user.total_points,
                rank=rank
            )
        
        leaderboard = Leaderboard.objects.all().order_by('rank')
        serializer = self.get_serializer(leaderboard, many=True)
        return Response(serializer.data)


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    
    def get_queryset(self):
        queryset = Workout.objects.all()
        difficulty = self.request.query_params.get('difficulty', None)
        if difficulty is not None:
            queryset = queryset.filter(difficulty=difficulty)
        return queryset
