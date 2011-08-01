from unittest import TestCase


from sqldiff.mixer import Mixer
from sqldiff.schema import Schema, Table, Column
from sqldiff.parser import SQLStmt



class MixerTest(TestCase):


    def test_factories(self):
        """
        By default, the mixer uses the following factories
        """
        m = Mixer()
        self.assertEqual(m.sqlParser, SQLStmt)
        self.assertEqual(m.schemaFactory, Schema)
        self.assertEqual(m.tableFactory, Table)
        self.assertEqual(m.columnFactory, Column)