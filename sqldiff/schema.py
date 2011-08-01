





class Table:
    """
    I am a database table.
    
    @ivar name: Name of the table
    @ivar columns: List of columns I have.
    """
    
    name = None
    
    
    def __init__(self, name=None):
        self.name = name
        self.columns = []



class Schema:
    """
    I am a database schema.
    
    @ivar name: Name of schema
    @ivar tables: List of L{Tables<Table>} defined in me.
    """


    name = None

    
    def __init__(self):
        self.tables = []


    def addTable(self, table):
        """
        Adds a table to this schema
        """
        self.tables.append(table)
        



class Column:
    """
    I am a column in a database L{Table}.
    
    @ivar name: Name of the column
    @ivar data_type: Data type of the column
    """
    
    name = None
    data_type = None