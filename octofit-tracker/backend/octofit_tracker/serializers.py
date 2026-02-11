from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'email', 'team', 'total_points']
    
    def get_id(self, obj):
        return str(obj._id) if obj._id else None


class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'members_count', 'total_points']
    
    def get_id(self, obj):
        return str(obj._id) if obj._id else None


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Activity
        fields = ['id', 'user_email', 'user', 'activity_type', 'duration', 'distance', 'points', 'date']
    
    def get_id(self, obj):
        return str(obj._id) if obj._id else None
    
    def get_user(self, obj):
        try:
            user = User.objects.get(email=obj.user_email)
            return user.username or user.name
        except User.DoesNotExist:
            return obj.user_email


class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = serializers.CharField(source='user_name')
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_email', 'user', 'user_name', 'team', 'total_points', 'activity_count', 'rank']
    
    def get_id(self, obj):
        return str(obj._id) if obj._id else None


class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty', 'duration', 'points']
    
    def get_id(self, obj):
        return str(obj._id) if obj._id else None
