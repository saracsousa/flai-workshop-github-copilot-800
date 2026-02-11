from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    total_points = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.name


class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    members_count = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    points = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'activities'
    
    def __str__(self):
        return f"{self.user_email} - {self.activity_type}"


class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user_email = models.EmailField()
    user_name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    total_points = models.IntegerField()
    rank = models.IntegerField()
    
    class Meta:
        db_table = 'leaderboard'
    
    def __str__(self):
        return f"{self.rank}. {self.user_name}"


class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)
    duration = models.IntegerField()  # in minutes
    points = models.IntegerField()
    
    class Meta:
        db_table = 'workouts'
    
    def __str__(self):
        return self.name
