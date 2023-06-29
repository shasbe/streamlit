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
st.write (con.sql("SHOW DATABASES").show())
#con.sql("SELECT * FROM 's3://sudsomni1/sales_demo.csv'").show()
