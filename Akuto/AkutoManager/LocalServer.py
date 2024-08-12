import sqlite3

class LocalServer:
    def __init__(self):
        # Loading/Conecting Databse
        self.connection = sqlite3.connect("Database") 
        self.cursor = self.connection.cursor() 

    def createDbTable(self):
            # Creates the main table.
           
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS produtos(nome, linha, quantidade)")
            self.connection.commit()
            
            print("\n dev note: createDbTable script ran successfully. \n ")


    def searchDb(self, nome = None, linha = None, quantidade = None):
        #print("\n dev note: searchDb scrit ran successfully. \n")
        # Search for products in the database.
        
        
        # All search options are empty by default.
        query = "SELECT * FROM produtos WHERE 1=1" # Original query                      <------------- |
        params = [] # Empty query list that forms the full query search                  <------------- |
 
        if nome is not None:              # If "N/L/Q" are filled with any letter -->                   |
             query += " AND nome LIKE ?"  #                                         |                   |
             params.append(f"%{nome}%")   # append "N/L/Q"L to the search query   <--                   |
                                                                 #/.\                                   |
        if linha is not None:                                    # |                                    |
             query += " AND linha LIKE ?"                        # |                                    |
             params.append(f"%{linha}%")                         # |                                    |
                                                                 # |                                    |
        if quantidade is not None:                               # |                                    |
             query += " AND quantidade LIKE ?"                   # |                                    |
             params.append(f"%{quantidade}%")                    # |                                    |
                                                                 #\./                                   |
        self.cursor.execute(query, params) # Tell the cursor that points to the server to execute query + list of any params filled:
        results = self.cursor.fetchall()   # Store the results into a variable
        self.connection.commit()           # Send all the previous command to the database

        return results
    
if __name__ == "__main__": 
     dataBase = LocalServer()

