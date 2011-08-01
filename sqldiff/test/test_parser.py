from unittest import TestCase


from sqldiff.parser import SQLStmt


class SqlStmtTest(TestCase):


    def t(self, sql, expected):
        """
        @param sql: An sql statement
        
        @type expected: dict
        @param expected: A dictionary of return values expected
        """
        r = SQLStmt.parseString(sql)
        for k, v in expected.items():
            if not hasattr(r, k):
                self.fail("Missing key: %r (value:%r)" % (k, v))
            actual = getattr(r, k)
            self.assertEqual(actual, v, "Expected %r instead of %r for %r" %
                             (v, k, actual))


    def test_create(self):
        """
        Basic create statement
        """
        sql = 'create table foo (id integer, bar text);'
        r = SQLStmt.parseString(sql)
        
        self.assertEqual(r.command, 'create')
        self.assertEqual(r.create_subcommand, 'table')
        self.assertEqual(r.table_name, 'foo')
        self.assertEqual(len(r.columns), 2)
        self.assertEqual(r.columns[0].name, 'id')
        self.assertEqual(r.columns[0].data_type, 'integer')
        self.assertEqual(r.columns[1].name, 'bar')
        self.assertEqual(r.columns[1].data_type, 'text')



