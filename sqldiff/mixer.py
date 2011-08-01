"""
I take the results of the parser and translate them into schema.
"""

from sqldiff import parser, schema


class Mixer:
    """
    I mix parser.SQLStmt and schema stuff.
    """
    
    sqlParser = parser.SQLStmt
    
    schemaFactory = schema.Schema
    tableFactory = schema.Table
    columnFactory = schema.Column