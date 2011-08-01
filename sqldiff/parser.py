
from pyparsing import (Keyword, CaselessKeyword, Word, alphas, alphanums,
                       delimitedList, Group)


CREATE = CaselessKeyword('create')
TABLE = CaselessKeyword('table')


ident = Word(alphas, alphanums + "_$")




# column def
column_def = Group(ident('name') + ident('data_type'))




# CREATE TABLE
create_table_stmt = CREATE('command') + TABLE('create_subcommand') + \
                    ident('table_name') + \
                    "(" + \
                    Group(delimitedList(column_def))('columns') + \
                    ")" + ";"



SQLStmt = create_table_stmt