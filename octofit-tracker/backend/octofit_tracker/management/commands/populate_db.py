from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting existing data...')
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write('Creating teams...')
        
        # Create teams
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='The mightiest heroes of Earth assembled to protect the world from threats too big for any one hero',
            members_count=0,
            total_points=0
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='The Justice League defending truth, justice, and protecting Earth from powerful villains',
            members_count=0,
            total_points=0
        )
        
        self.stdout.write('Creating users...')
        
        # Create Marvel superhero users
        marvel_heroes = [
            {'name': 'Iron Man', 'username': 'ironman', 'email': 'ironman@marvel.com'},
            {'name': 'Captain America', 'username': 'capamerica', 'email': 'captainamerica@marvel.com'},
            {'name': 'Thor', 'username': 'thor_odinson', 'email': 'thor@marvel.com'},
            {'name': 'Hulk', 'username': 'hulk_smash', 'email': 'hulk@marvel.com'},
            {'name': 'Black Widow', 'username': 'blackwidow', 'email': 'blackwidow@marvel.com'},
            {'name': 'Spider-Man', 'username': 'spidey', 'email': 'spiderman@marvel.com'},
            {'name': 'Doctor Strange', 'username': 'drstrange', 'email': 'doctorstrange@marvel.com'},
            {'name': 'Black Panther', 'username': 'blackpanther', 'email': 'blackpanther@marvel.com'},
        ]
        
        # Create DC superhero users
        dc_heroes = [
            {'name': 'Superman', 'username': 'superman', 'email': 'superman@dc.com'},
            {'name': 'Batman', 'username': 'batman', 'email': 'batman@dc.com'},
            {'name': 'Wonder Woman', 'username': 'wonderwoman', 'email': 'wonderwoman@dc.com'},
            {'name': 'The Flash', 'username': 'flash', 'email': 'flash@dc.com'},
            {'name': 'Aquaman', 'username': 'aquaman', 'email': 'aquaman@dc.com'},
            {'name': 'Green Lantern', 'username': 'greenlantern', 'email': 'greenlantern@dc.com'},
            {'name': 'Cyborg', 'username': 'cyborg', 'email': 'cyborg@dc.com'},
            {'name': 'Shazam', 'username': 'shazam', 'email': 'shazam@dc.com'},
        ]
        
        marvel_users = []
        dc_users = []
        
        for hero in marvel_heroes:
            user = User.objects.create(
                username=hero['username'],
                name=hero['name'],
                email=hero['email'],
                team='Team Marvel',
                total_points=0
            )
            marvel_users.append(user)
        
        for hero in dc_heroes:
            user = User.objects.create(
                username=hero['username'],
                name=hero['name'],
                email=hero['email'],
                team='Team DC',
                total_points=0
            )
            dc_users.append(user)
        
        # Update team member counts
        team_marvel.members_count = len(marvel_users)
        team_marvel.save()
        team_dc.members_count = len(dc_users)
        team_dc.save()
        
        self.stdout.write('Creating workouts...')
        
        # Create workouts
        workouts_data = [
            {'name': 'Avengers Assemble', 'description': 'High-intensity team workout', 'difficulty': 'Hard', 'duration': 60, 'points': 100},
            {'name': 'Shield Training', 'description': 'Core and upper body workout', 'difficulty': 'Medium', 'duration': 45, 'points': 75},
            {'name': 'Web Slinger', 'description': 'Agility and flexibility training', 'difficulty': 'Medium', 'duration': 30, 'points': 50},
            {'name': 'Hulk Smash', 'description': 'Power lifting session', 'difficulty': 'Hard', 'duration': 45, 'points': 80},
            {'name': 'Mjolnir Lift', 'description': 'Strength training workout', 'difficulty': 'Hard', 'duration': 50, 'points': 85},
            {'name': 'Justice League Unite', 'description': 'Full body workout', 'difficulty': 'Hard', 'duration': 60, 'points': 100},
            {'name': 'Batcave Training', 'description': 'Stealth and cardio workout', 'difficulty': 'Medium', 'duration': 40, 'points': 70},
            {'name': 'Speed Force', 'description': 'High-speed cardio session', 'difficulty': 'Easy', 'duration': 20, 'points': 40},
            {'name': 'Kryptonian Strength', 'description': 'Ultimate strength workout', 'difficulty': 'Hard', 'duration': 55, 'points': 90},
            {'name': 'Amazon Warrior', 'description': 'Combat training workout', 'difficulty': 'Medium', 'duration': 45, 'points': 75},
        ]
        
        workouts = []
        for workout_data in workouts_data:
            workout = Workout.objects.create(**workout_data)
            workouts.append(workout)
        
        self.stdout.write('Creating activities...')
        
        # Create activities for all users
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Boxing', 'Martial Arts']
        all_users = marvel_users + dc_users
        
        for user in all_users:
            # Create 5-10 activities per user over the past 30 days
            num_activities = random.randint(5, 10)
            user_points = 0
            
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 90)
                
                # Add distance for running and cycling
                distance = 0.0
                if activity_type == 'Running':
                    distance = round(random.uniform(3.0, 15.0), 2)  # 3-15 km
                elif activity_type == 'Cycling':
                    distance = round(random.uniform(10.0, 50.0), 2)  # 10-50 km
                elif activity_type == 'Swimming':
                    distance = round(random.uniform(0.5, 3.0), 2)  # 0.5-3 km
                
                points = duration // 2  # Simple points calculation
                date = datetime.now() - timedelta(days=random.randint(0, 30))
                
                Activity.objects.create(
                    user_email=user.email,
                    activity_type=activity_type,
                    duration=duration,
                    distance=distance if distance > 0 else None,
                    points=points,
                    date=date
                )
                
                user_points += points
            
            # Update user total points
            user.total_points = user_points
            user.save()
        
        # Update team total points
        team_marvel.total_points = sum(user.total_points for user in marvel_users)
        team_marvel.save()
        
        team_dc.total_points = sum(user.total_points for user in dc_users)
        team_dc.save()
        
        self.stdout.write('Creating leaderboard...')
        
        # Create leaderboard entries
        all_users_sorted = sorted(all_users, key=lambda u: u.total_points, reverse=True)
        
        for rank, user in enumerate(all_users_sorted, start=1):
            activity_count = Activity.objects.filter(user_email=user.email).count()
            Leaderboard.objects.create(
                user_email=user.email,
                user_name=user.username,
                team=user.team,
                total_points=user.total_points,
                activity_count=activity_count,
                rank=rank
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data!'))
        self.stdout.write(f'Created {len(marvel_users)} Marvel heroes and {len(dc_users)} DC heroes')
        self.stdout.write(f'Team Marvel total points: {team_marvel.total_points}')
        self.stdout.write(f'Team DC total points: {team_dc.total_points}')
