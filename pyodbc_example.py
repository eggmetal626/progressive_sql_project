# python module used to connect to microsoft sql (MS SQL) databases
import pyodbc


class Connector():
  
  def __init__(self) -> None:
    """ Constructor for the helper class. 
        User id's and passwords should never be stored in code, 
        so I've put in placeholder values below"""
    
    self.driver = "ODBC Driver 17 for SQL Server"
    self.server_and_port = "fakeservername,3306"
    self.user_id = "fakeusername"
    self.password = "fakepassword"
    self.cnxn = None
    
  def run_query(self, query) -> list:
    
    try:
      self.cnxn = pyodbc.connect(self.cnxstr, autocommit=True)
    except pyodbc.Error as e:
      print("Connection failed")
    with self.cnxn as db_connect: # using the with keyword automatically opens and closes the database connection
      print("Connection succeeded!")
      cursor = db_connect.cursor() # used to move thru the data
      cursor.execuate(query)
      row = cursor.fetchone()
      
      while row: #loops thru the rows
        row = cursor.fetchone()
        print(f"row: {row}")
        
        
if __name__ = "__main__":
  # where python begins to run code
  
  # it is difficult to make an sql query without actually having real column names
  # so instead I've made this query to have some fun 
  # and to demonstrate that I know various MS SQL keywords
  job_query_for_chris = """
    SELECT
    *
    FROM
    jobs.ThatIWant
    INNER JOIN
    jobs.ThatImQualifiedFor
    WHERE companies.Name = "Progressive"
    AND jobNumbers.ThatImQualifiedFor = "200536"
  """
  
  connector = Connector()
  connector.run_query(job_query_for_chris)
          
