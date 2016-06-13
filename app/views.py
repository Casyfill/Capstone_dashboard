from flask import render_template, flash, redirect
from app import app
from .forms import Add_Records_Form

@app.route('/')
@app.route('/index')

def index():   
    return render_template('index.html',
                           title='Home',
                           crimes=app.config['CRIME_RECORDS']
                           )

@app.route('/add_record', methods=['GET', 'POST'])
def submitRecord():
    form = Add_Records_Form()
    error = None
    
    if form.validate_on_submit():
        flag = 0
        for c in app.config['CRIME_RECORDS']:
            if c['crimeId']==form.crimeId.data:
                flag = 1
                print flag
        if flag == 0:
            app.config['CRIME_RECORDS'].append({'crimeId': form.crimeId.data, 'modeOfEntry': form.modeOfEntry.data})
            return redirect('../add_record')
        else:
            flash('Duplicated CrimeID!')
    elif form.crimeId.data=='' or form.modeOfEntry.data=='':
        flash('Incomplete record entries!')
    return render_template('add_record.html', 
                           title='Add Record',
                           form=form,
                           crime_records=app.config['CRIME_RECORDS']
                          )