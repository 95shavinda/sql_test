import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("SELECT username,rank FROM users WHERE rank = '{0}'".format(rank))


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
    
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():

    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))

    conn.commit()
    
#create_table()
#data_entry()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
c.close
conn.close()