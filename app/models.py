from app import db
from sqlalchemy.dialects.postgresql import JSON
import sqlalchemy

# this class used to initialize table datatypes,
# which has been done in folder raw_data_processing/to_database.py
# class Test(db.Model):
#     __tablename__ = 'test'

    # id = db.Column(db.Integer, primary_key=True)
    # result_all = db.Column(JSON)
    # result_no_stop_words = db.Column(JSON)
              
    # dtDict = {'EVENT_ID': sqlalchemy.types.NUMERIC,
    #       'DATETIME_FROM':sqlalchemy.types.DateTime,
    #       'DATETIME_TO':sqlalchemy.types.DateTime,
    #       'LOC_X': sqlalchemy.types.NUMERIC,
    #       'LOC_Y': sqlalchemy.types.NUMERIC,
    #       'PR_CODE':sqlalchemy.types.NUMERIC,
    #       'BLD_TYPE':sqlalchemy.types.String
    #       }          

    # def __init__(self, result_all, result_no_stop_words):
    #     self.result_all = result_all
    #     self.result_no_stop_words = result_no_stop_words

    # def __repr__(self):
    #     return '<EVENT_ID {}>'.format(self.EVENT_ID)