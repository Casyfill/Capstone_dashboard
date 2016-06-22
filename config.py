# it activates the cross-site request forgery prevention (note that this setting is enabled by default in current versions of Flask-WTF). In most cases you want to have this option enabled as it makes your app more secure
WTF_CSRF_ENABLED = True

# this is only needed when CSRF is enabled, and is used to create a cryptographic token that is used to validate a form. When you write your own apps make sure to set the secret key to something that is difficult to guess.
SECRET_KEY = 'you-will-never-guess'

# previously hardcoded records
#CRIME_RECORDS = [
#        {
#            'crimeId':'12',
#            'modeOfEntry': 'Front Door'
#        },
#        {
#            'crimeId':'43',
#            'modeOfEntry': 'Side Window'
#        },
#        {
#            'crimeId':'78',
#            'modeOfEntry': 'Back Door'
#        },
#        {
#            'crimeId':'54',
#            'modeOfEntry': 'Front Door'
#        }
#    ]


import psycopg2
import psycopg2.extras
import sys
import pprint
import pandas as pd


conn_str = "host='localhost' dbname='myevents' user='ubuntu' password='123'"
print "Connecting to database-> %s" % (conn_str)

# get a connection
conn = psycopg2.connect(conn_str)

# conn.cursor will return a cursor object, you can use this query to perform queries
# note that in this example we pass a cursor_factory argument that will
# dictionary cursor so COLUMNS will be returned as a dictionary so we
# can access columns by their name instead of index.
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute('SELECT * FROM test')
EVENT_RECORDS = cursor.fetchall()
COLNAME = [desc[0] for desc in cursor.description]
#print [crime[i]['datetime_from'] for i in range(len(crime))]












