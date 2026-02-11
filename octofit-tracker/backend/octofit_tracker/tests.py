from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Test Team", members_count=1, total_points=0)
        self.user = User.objects.create(
            name="Test User",
            email="test@example.com",
            team="Test Team",
            total_points=0
        )
    
    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.team, "Test Team")
        self.assertEqual(self.user.total_points, 0)
    
    def test_user_string_representation(self):
        """Test user string representation"""
        self.assertEqual(str(self.user), "Test User")


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name="Test Team",
            members_count=5,
            total_points=100
        )
    
    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, "Test Team")
        self.assertEqual(self.team.members_count, 5)
        self.assertEqual(self.team.total_points, 100)
    
    def test_team_string_representation(self):
        """Test team string representation"""
        self.assertEqual(str(self.team), "Test Team")


class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user_email="test@example.com",
            activity_type="Running",
            duration=30,
            points=50
        )
    
    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.user_email, "test@example.com")
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.points, 50)


class UserAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'name': 'API Test User',
            'email': 'apitest@example.com',
            'team': 'API Test Team',
            'total_points': 0
        }
    
    def test_create_user(self):
        """Test creating a user via API"""
        response = self.client.post(reverse('user-list'), self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'API Test User')
    
    def test_get_users(self):
        """Test retrieving users via API"""
        User.objects.create(**self.user_data)
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class TeamAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.team_data = {
            'name': 'API Test Team',
            'members_count': 0,
            'total_points': 0
        }
    
    def test_create_team(self):
        """Test creating a team via API"""
        response = self.client.post(reverse('team-list'), self.team_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)
    
    def test_get_teams(self):
        """Test retrieving teams via API"""
        Team.objects.create(**self.team_data)
        response = self.client.get(reverse('team-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class WorkoutAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout_data = {
            'name': 'Test Workout',
            'description': 'A test workout',
            'difficulty': 'beginner',
            'duration': 20,
            'points': 30
        }
    
    def test_create_workout(self):
        """Test creating a workout via API"""
        response = self.client.post(reverse('workout-list'), self.workout_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Workout.objects.count(), 1)
    
    def test_get_workouts(self):
        """Test retrieving workouts via API"""
        Workout.objects.create(**self.workout_data)
        response = self.client.get(reverse('workout-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class APIRootTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_api_root(self):
        """Test API root endpoint"""
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
