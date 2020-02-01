import time
"""python module that makes our app sleep for a few seconds in between each db check """
from django.db import connections
"""this checks if db connection is availabe"""
from django.db.utils import OperationalError
"""erro that DB through if not availabe"""
from django.core.management.base import BaseCommand
"""class that allows us to build our custom command"""


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
