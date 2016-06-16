#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine
import sys

def process_data(path, username, password, dbase, tablename, dtDict):
    df = pd.read_csv(path)
    df.columns = [c.lower().replace(' ','_') for c in df.columns] #postgres doesn't like capitals or spaces
    engine = create_engine('postgresql://{0}:{1}@localhost:5432/{2}'.format(username, password, dbase))

    df.to_sql(tablename, 
              engine, 
             index=False, #Do not output the index of the datafram
              index=False, #Do not output the index of the datafram
              dtype=dtDict) #Datatypes should be [sqlalchemy types][1]
    print 'done! data is in the database!'


if __name__ == '__main__':
    if len(sys.argv)<2:
        raise IOError('Need path to file to be specified!')
    
    dtDict = {'EVENT_ID': sqlalchemy.types.NUMERIC,
              'DATETIME_FROM':,
              'DATETIME_TO':,
              'LOC_X': sqlalchemy.types.NUMERIC,
              'LOC_Y':,
              'PR_CODE':,
              'BLD_TYPE:'
              }
        
    process_data(sys.argv[1], 
                 username='seuen', 
                 password='999',
                 dbase='events',
                 tablename='test',
                 dtDict)


                 'col2': sqlalchemy.types.String