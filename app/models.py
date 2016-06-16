from app import db
from sqlalchemy.dialects.postgresql import JSON


class Event(db.Model):
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True)
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, result_all, result_no_stop_words):
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)