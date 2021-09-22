import sqlite3
import os
# import random number generator
import pandas as pd
from numpy.random import uniform

random_numbers = uniform(low=10.0, high=25.0, size=100000)



connection = sqlite3.connect("/Users/hectorprado/Desktop/CodeCademy/Data_Analytics/Projects/databases/original.db")
cursor = connection.cursor()
#cursor.execute("CREATE TABLE Pressure (reading float not null)")
query = "INSERT INTO Pressure (reading) VALUES (?);"


#cursor.execute("INSERT INTO Pressure Values(100.00)")
cursor.execute("SELECT * FROM Pressure;")
result = cursor.fetchall()
print(result)
"""
new_df = pd.read_sql_table("Pressure", connection)

print(new_df)
"""

cursor.close()
# save changes to file for next exercise
connection.commit()
connection.close()