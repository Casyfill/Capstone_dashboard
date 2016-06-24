import psycopg2
import psycopg2.extras
import sys
import pprint
import pandas as pd
import numpy as np
from flask import render_template, flash, redirect, request
from app import app
from .forms import Search_Records_Form

@app.route('/')
@app.route('/index')

def index():  
    cursor = connect_db()
    cursor.execute('SELECT * FROM test')
    EVENT_RECORDS = cursor.fetchall()
    COLNAME = [desc[0] for desc in cursor.description]
    
    return render_template('index.html',
                           title='Home',
                           events=EVENT_RECORDS,
                           colnames=COLNAME
                           )

@app.route('/search_record', methods=['GET', 'POST'])
def searchRecord():
    # define variables
    form = Search_Records_Form()
    resultDict = {}
    
    # check if the request method is POST (where form helps retrieve info from backend)
    if request.method.upper()=='POST':
        event = []
        events_updated = []
        colnames = []
        
        # check if enter value is null
        if len(form.event_id.data)==0:
            flash('Empty Entry!')
            print "Empty entry"
        else:   # INFO         
            # execute query for [Info] button
            query = 'SELECT * FROM test WHERE %s=%s'%('event_id', form.event_id.data)
            
            # retrieve data records from database
            cursor = connect_db()
            cursor.execute(query)
            resultDict['event'] = cursor.fetchall() 
            
            if len(resultDict['event'])==0:
                flash('No such event')

            else:
                resultDict['event_colnames'] = [desc[0] for desc in cursor.description]

            if request.form['button']=="Search":  # SEARCH              
                # execute query for [Search] button
                query = 'SELECT * FROM test WHERE %s=%s'%('relavence', form.event_id.data)
                
                # retrieve data records from database
                cursor = connect_db()
                cursor.execute(query)
                resultDict['events_updated'] = cursor.fetchall() 
                 
                if len(resultDict['events_updated'])==0:
                    flash('No relavent events!')
                else:
                    resultDict['events_colnames'] = [desc[0] for desc in cursor.description]
                    
        return render_template('search_record.html',
                               title='Records',
                               form=form,
                               resultDict=resultDict
                               )
    else:
        return render_template('search_record.html',
                               title='Records',
                               form=form,
                               resultDict=resultDict
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
