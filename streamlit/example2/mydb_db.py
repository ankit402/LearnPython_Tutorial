import sqlite3, streamlit as st, ast

con = sqlite3.connect('mydb.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS db_new(name TEXT)')
con.commit()
cur.execute('INSERT into db_new(name) values (?)', ('new',))
con.commit()
test = cur.execute('SELECT name FROM db_new').fetchall()
tupledata=[]
for newdata in test:
    tupledata = (newdata[0])
selecteddata=st.selectbox('Select an tuple', tupledata)
with st.form("Create or Update a Row of Data", clear_on_submit=True):
    if st.form_submit_button("Submit"):
        cur.execute(f'''DELETE FROM db WHERE name="{selecteddata}";''')
        con.commit()
        st.write(f"{selecteddata} has been deleted")
        st.write(len(tupledata))
startdate= st.date_input('Start Date')
enddata= st.date_input('End Date')
if startdate and enddata:
    st.write("Should not be same")