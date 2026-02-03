from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete all existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create users (superheroes)
        marvel_heroes = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'first_name': 'Tony', 'last_name': 'Stark'},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'first_name': 'Steve', 'last_name': 'Rogers'},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'first_name': 'Peter', 'last_name': 'Parker'},
        ]
        dc_heroes = [
            {'username': 'batman', 'email': 'batman@dc.com', 'first_name': 'Bruce', 'last_name': 'Wayne'},
            {'username': 'superman', 'email': 'superman@dc.com', 'first_name': 'Clark', 'last_name': 'Kent'},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'first_name': 'Diana', 'last_name': 'Prince'},
        ]
        marvel_users = [User.objects.create(**hero) for hero in marvel_heroes]
        dc_users = [User.objects.create(**hero) for hero in dc_heroes]

        # Create teams
        marvel_team = Team.objects.create(name='Team Marvel')
        marvel_team.members.set(marvel_users)
        dc_team = Team.objects.create(name='Team DC')
        dc_team.members.set(dc_users)

        # Create workouts
        workout1 = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='Strength')
        workout2 = Workout.objects.create(name='Running', description='Run 5km', suggested_for='Endurance')

        # Create activities
        Activity.objects.create(user=marvel_users[0], activity_type='Pushups', duration=10, calories_burned=50, date=timezone.now().date())
        Activity.objects.create(user=dc_users[0], activity_type='Running', duration=30, calories_burned=300, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(team=marvel_team, points=150)
        Leaderboard.objects.create(team=dc_team, points=200)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
