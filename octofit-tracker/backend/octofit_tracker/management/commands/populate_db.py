

from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **options):
        # Clear existing data using raw MongoDB
        db = connection.cursor().db_conn
        db['user'].delete_many({})
        db['team'].delete_many({})
        db['activity'].delete_many({})
        db['leaderboard'].delete_many({})
        db['workout'].delete_many({})

        # Create teams
        marvel = Team.objects.create(id=str(ObjectId()), name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(id=str(ObjectId()), name='DC', description='DC Superheroes')

        # Create users
        ironman = User.objects.create(id=str(ObjectId()), name='Iron Man', email='ironman@marvel.com', team='Marvel')
        captain = User.objects.create(id=str(ObjectId()), name='Captain America', email='cap@marvel.com', team='Marvel')
        batman = User.objects.create(id=str(ObjectId()), name='Batman', email='batman@dc.com', team='DC')
        superman = User.objects.create(id=str(ObjectId()), name='Superman', email='superman@dc.com', team='DC')

        # Create activities
        Activity.objects.create(id=str(ObjectId()), user=ironman, type='Run', duration=30, date='2025-08-20')
        Activity.objects.create(id=str(ObjectId()), user=batman, type='Swim', duration=45, date='2025-08-21')
        Activity.objects.create(id=str(ObjectId()), user=superman, type='Bike', duration=60, date='2025-08-22')
        Activity.objects.create(id=str(ObjectId()), user=captain, type='Yoga', duration=20, date='2025-08-19')

        # Create leaderboard
        Leaderboard.objects.create(id=str(ObjectId()), team=marvel, points=150)
        Leaderboard.objects.create(id=str(ObjectId()), team=dc, points=120)

        # Create workouts
        Workout.objects.create(id=str(ObjectId()), name='Pushups', description='Do 20 pushups', suggested_for='Marvel')
        Workout.objects.create(id=str(ObjectId()), name='Plank', description='Hold plank for 1 minute', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
