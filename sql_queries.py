sqlserver_extract = ('''
  SELECT sqlserver_column_1, sqlserver_column_2, sqlserver_column_3
  FROM sqlserver_table
''')

sqlserver_insert = ('''
  INSERT INTO table (column_1, column_2, column_3)
  VALUES (?, ?, ?)  
''')

# exporting queries
class SqlQuery:
  def __init__(self, extract_query, load_query):
    self.extract_query = extract_query
    self.load_query = load_query

# create instances for SqlQuery class
sqlserver_query = SqlQuery(sqlserver_extract, sqlserver_insert)

# store as list for iteration
sqlserver_queries = [sqlserver_query]