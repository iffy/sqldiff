from unittest import TestCase


from sqldiff.schema import Table, Schema, Column



class ColumnTest(TestCase):


    def test_attrs(self):
        """
        Columns should have these attributes
        """
        c = Column()
        self.assertEqual(c.name, None)
        self.assertEqual(c.data_type, None)



class TableTest(TestCase):


    def test_attrs(self):
        """
        Should have these attributes
        """
        t = Table()
        self.assertEqual(t.name, None)
        self.assertEqual(t.columns, [])



class SchemaTest(TestCase):

    
    def test_attrs(self):
        """
        Schema should have these attributes
        """
        s = Schema()
        self.assertEqual(s.name, None)
        self.assertEqual(s.tables, [])


    def test_addTable(self):
        """
        Adds an object to the tables list
        """
        sql = 'create table foo (id integer);'
        s = Schema()
        table = Table()
        s.addTable(table)
        self.assertEqual(s.tables, [table])        
        