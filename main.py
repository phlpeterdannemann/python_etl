import pyodbc
# variables
from db_credentials import datawarehouse_db_config, sqlserver_db_config
from sql_queries import sqlserver_queries
from variables import *
# methods
from etl import etl_process


def main():
  print('starting etl')
	
  # establish connection for target database (sql-server)
  target_cnx = pyodbc.connect(**datawarehouse_db_config)
	
  # loop through credentials
	
  # sql-server
  for config in sqlserver_db_config: 
    try:
      print("loading db: " + config['database'])
      etl_process(sqlserver_queries, target_cnx, config, 'sqlserver')
    except Exception as error:
      print("etl for {} has error".format(config['database']))
      print('error message: {}'.format(error))
      continue
	
  target_cnx.close()

if __name__ == "__main__":
  main()