from flask import render_template, flash, redirect
from app import app

@app.route('/')
@app.route('/index')

def index():
    crimes = [
        {
            'ID':'12',
            'Mode_Entry': 'Front Door'
        },
        {
            'ID':'43',
            'Mode_Entry': 'Side Window'
        },
        {
            'ID':'78',
            'Mode_Entry': 'Back Door'
        }
    ]
   
    return render_template("index.html",
                           title='Home',
                           crimes=crimes)