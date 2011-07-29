from unittest import TestCase


from sqldiff.schema import Table



class TableTest(TestCase):


    def test_attrs(self):
        """
        Should have these attributes
        """
        t = Table()
        self.assertEqual(t.name, None)
        self.assertEqual(t.columns, [])
