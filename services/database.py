import pyodbc 
server = 'localhost' 
database = 'crud_python' 
username = 'iago' 
password = 'vitoriaamor12' 
cnxn = pyodbc.connect('DRIVER={MySQL ODBC 3.51 Driver};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()