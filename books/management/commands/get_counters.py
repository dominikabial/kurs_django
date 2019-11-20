from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll
from django_redis import get_redis_connection
class Command(BaseCommand):
    help = "Pobiera liczniki"


    def handle(self, *args, **options):
        con = get_redis_connection()
        keys = con.keys()
        print("liczniki pobran")
        for k in keys:
            print(k.decode(), ":", con.get(k).decode())