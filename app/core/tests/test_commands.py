from unittest.mock import patch
"""this will allow is to mock the behavior of the Django Git db function"""
"""basiclly this will similate when the DB is availabe or not avilabe for our command"""
from django.core.management import call_command
"""this will allow us to call the command in our src code"""
from django.db.utils import OperationalError
"""the error that Django throughs when the DB is not availabe"""
from django.test import TestCase
"""testcase"""


class CommandsTestCase(TestCase):

    def test_wait_for_db_ready(self):
        """when we call the command the DB is already availabe """
        """Test waiting for db when db is available"""
        """we need to similate when the DB is avialbe"""
        """if thier is a operational error we know it failed, no error it passed"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            """here we are returning a value true for every call with value true"""
            gi.return_value = True
            """calling command"""
            call_command('wait_for_db')
            """we need just 1 """
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=None)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
