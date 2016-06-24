import psycopg2
import psycopg2.extras
import sys
import pprint
import pandas as pd
from flask import render_template, flash, redirect, request
from app import app
from .forms import Search_Records_Form

@app.route('/')
@app.route('/index')

def index():  
#    COLNAME, EVENT_RECORDS = connect_db('SELECT * FROM test')
    cursor = connect_db()
    EVENT_RECORDS = cursor.fetchall()
    cursor.execute('SELECT * FROM test')
    COLNAME = [desc[0] for desc in cursor.description]
    
    return render_template('index.html',
                           title='Home',
                           events=EVENT_RECORDS,
                           colnames=COLNAME
                           )

@app.route('/search_record', methods=['GET', 'POST'])
def searchRecord():
    # define form
    form = Search_Records_Form()
    error = None
    
    # retrieve data records from database
    cursor = connect_db()
    colnames = []
    
    # check if the request method is POST (where form helps retrieve info from backend)
    if request.method.upper()=='POST':
        # select one of the two functions to react on (based on which button you click)
        if request.form['button']=="Search":
            cursor.execute('SELECT * FROM test WHERE relavence=%s'% form.event_id.data)
            events_updated = cursor.fetchall()
            colnames = [desc[0] for desc in cursor.description]

        elif request.form['button']=="Info":
            cursor.execute('SELECT * FROM test WHERE event_id=%s'%form.event_id.data)
            events_updated = cursor.fetchall()
            colnames = [desc[0] for desc in cursor.description]
        else:
            flash('Wrong button!')
            return redirect('../search_record')

    return render_template('search_record.html',
                           title='Records',
                           form=form,
                           events=events_updated,
                           colnames=colnames
                           )

def connect_db():
    # define connection
    conn_str = "host='localhost' dbname='myevents' user='ubuntu' password='123'"
    print "Connecting to database-> %s" % (conn_str)

    # get a connection
    conn = psycopg2.connect(conn_str)

    # conn.cursor will return a cursor object, you can use this query to perform queries
    # note that in this example we pass a cursor_factory argument that will
    # dictionary cursor so COLUMNS will be returned as a dictionary so we
    # can access columns by their name instead of index.
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)    
    return cursor
