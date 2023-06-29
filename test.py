import duckdb
import streamlit as st
import pandas as pd
import numpy as np

st.title('Sales Data from S3')

conn = duckdb.connect('md:?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uIjoic2hhc2JlLmdtYWlsLmNvbSIsImVtYWlsIjoic2hhc2JlQGdtYWlsLmNvbSIsInVzZXJJZCI6ImU4NzhlMTJjLWZiYzAtNDJiMS05NjhlLWU3ZmJjMTk2NjQzYyIsImlhdCI6MTY4ODAwMzg2MSwiZXhwIjoxNzE5NTYxNDYxfQ.PTwhFvOt9h88AP7EzgU1g1ZidzBy-_Av0ZBXybSzflU')

# Perform a SELECT query
result = conn.execute("SELECT * FROM 's3://sudsomni1/sales_demo.csv'").df()

# Fetch all rows from the result set
#rows = result.fetchall()

# Display the retrieved data in Streamlit
st.write("Sales Data:")
st.write(result)

# Close the connection
conn.close()

