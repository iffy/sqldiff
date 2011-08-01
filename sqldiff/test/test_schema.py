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


    def test_init_name(self):
        """
        You can initialize with a name
        """
        t = Table('foo')
        self.assertEqual(t.name, 'foo')


    def test_init_columns(self):
        """
        You can initialize with a list of columns
        """
        c1 = Column()
        c2 = Column()
        t = Table('foo', [c1, c2])
        self.assertEqual(t.columns, [c1, c2])



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
        