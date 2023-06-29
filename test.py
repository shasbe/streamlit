import duckdb
import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in sea')

# initiate the MotherDuck connection through a service token through
#con = duckdb.connect('md:?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uIjoic2hhc2JlLmdtYWlsLmNvbSIsImVtYWlsIjoic2hhc2JlQGdtYWlsLmNvbSIsInVzZXJJZCI6ImU4NzhlMTJjLWZiYzAtNDJiMS05NjhlLWU3ZmJjMTk2NjQzYyIsImlhdCI6MTY4ODAwMzg2MSwiZXhwIjoxNzE5NTYxNDYxfQ.PTwhFvOt9h88AP7EzgU1g1ZidzBy-_Av0ZBXybSzflU')

# connect to your MotherDuck database through 'md:mydatabase' or 'motherduck:mydatabase'
# if the database doesn't exist, MotherDuck creates it when you connect
#con = duckdb.connect('md:mydatabase')

# run a query to check verify that you are connected
#response=con.sql("SHOW DATABASES").show()
st.write ("testing the stuff")
#con.sql("SELECT * FROM 's3://sudsomni1/sales_demo.csv'").show()


import duckdb
import streamlit as st

# Create a DuckDB connection
conn = duckdb.connect('md:?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uIjoic2hhc2JlLmdtYWlsLmNvbSIsImVtYWlsIjoic2hhc2JlQGdtYWlsLmNvbSIsInVzZXJJZCI6ImU4NzhlMTJjLWZiYzAtNDJiMS05NjhlLWU3ZmJjMTk2NjQzYyIsImlhdCI6MTY4ODAwMzg2MSwiZXhwIjoxNzE5NTYxNDYxfQ.PTwhFvOt9h88AP7EzgU1g1ZidzBy-_Av0ZBXybSzflU')
#conn = duckdb.connect(database=':memory:')

# Create a table
#conn.execute("CREATE TABLE employees (id INTEGER, name VARCHAR(100), salary FLOAT)")

# Insert some data into the table
#conn.execute("INSERT INTO employees VALUES (1, 'John Doe', 5000.0)")
#conn.execute("INSERT INTO employees VALUES (2, 'Jane Smith', 6000.0)")
#conn.execute("INSERT INTO employees VALUES (3, 'Alice Johnson', 7000.0)")

# Perform a SELECT query
#result = conn.execute("SELECT * FROM employees")
result = conn.execute("SELECT * FROM 's3://sudsomni1/sales_demo.csv'")

# Fetch all rows from the result set
rows = result.fetchall()

# Display the retrieved data in Streamlit
st.write("Sales Data:")
st.write(rows)

# Close the connection
conn.close()

