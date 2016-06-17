from app import db
from sqlalchemy.dialects.postgresql import JSON
import sqlalchemy

# this class used to initialize table datatypes,
# which has been done in folder raw_data_processing/to_database.py
# class Test(db.Model):
#     __tablename__ = 'test'

#     eventid = db.Column(db.NUMERIC, primary_key=True)
#     datetimefrom = db.Column(db.DateTime)
#     datetimeto = db.Column(db.DateTime)
#     locx = db.Column(db.NUMERIC)
#     locy = db.Column(db.NUMERIC)
#     prcode = db.Column(db.NUMERIC)
#     bldtype = db.Column(db.String)
    
#     # dtDict = {'eventid': sqlalchemy.types.NUMERIC,
#     #       'datetime from':sqlalchemy.types.DateTime,
#     #       'DATETIME_TO':sqlalchemy.types.DateTime,
#     #       'LOC_X': sqlalchemy.types.NUMERIC,
#     #       'LOC_Y': sqlalchemy.types.NUMERIC,
#     #       'PR_CODE':sqlalchemy.types.NUMERIC,
#     #       'BLD_TYPE':sqlalchemy.types.String
#     #       }          

#     def __init__(self, DATETIME_FROM, DATETIME_TO, LOC_X, LOC_Y, PR_CODE, BLD_TYPE):
#         self.datetimefrom = DATETIME_FROM
#         self.datetimefrom = DATETIME_TO
#         self.locx = LOC_X
#         self.locx = LOC_Y
#         self.prcode = PR_CODE
#         self.bldtype = BLD_TYPE
        
#     def __repr__(self):
#         return '<EVENT_ID {}>'.format(self.EVENT_ID)