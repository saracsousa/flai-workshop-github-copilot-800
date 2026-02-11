#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

print("Limpando banco de dados...")
User.objects.all().delete()
Team.objects.all().delete()
Activity.objects.all().delete()
Leaderboard.objects.all().delete()
Workout.objects.all().delete()
print("Banco de dados limpo com sucesso!")
