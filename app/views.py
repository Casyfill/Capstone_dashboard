from flask import render_template, flash, redirect, request
from app import app
from .forms import Add_Records_Form, Search_Records_Form

@app.route('/')
@app.route('/index')

def index():   
    return render_template('index.html',
                           title='Home',
                           events=app.config['EVENT_RECORDS'],
                           colnames=app.config['COLNAME']
                           )


@app.route('/search_record', methods=['GET', 'POST'])
def searchRecord():
    # define form
    form = Search_Records_Form()
    error = None
    
    # retrieve data records from database
    colnames=app.config['COLNAME']
    events=app.config['EVENT_RECORDS']
    
    # for views html
    events_updated = []
    seed = []
    
    if request.method.upper()=='POST':
        if request.form['button']=="Search":
            print "yes"
            for i in range(len(events)):
                if form.event_id.data in str(events[i]['relavence']):
                    events_updated.append(events[i])
        elif request.form['button']=="Info":
            for i in range(len(events)):
                if form.event_id.data in str(events[i]['event_id']):
                    events_updated.append(events[i])
        else:
            flash('Wrong button!')
            return redirect('../search_record')

    return render_template('search_record.html',
                           title='Records',
                           form=form,
                           events=events_updated,
                           colnames=colnames
                           )


@app.route('/add_record', methods=['GET', 'POST'])
def submitRecord():
    form = Add_Records_Form()
    error = None
    
    if form.validate_on_submit():
        flag = 0
        for c in app.config['EVENT_RECORDS']:
            if c['crimeId']==form.crimeId.data:
                flag = 1
                print flag
        if flag == 0:
            app.config['EVENT_RECORDS'].append({'crimeId': form.crimeId.data, 'modeOfEntry': form.modeOfEntry.data})
            return redirect('../add_record')
        else:
            flash('Duplicated EventID!')
    elif form.crimeId.data=='' or form.modeOfEntry.data=='':
        flash('Incomplete record entries!')
    return render_template('add_record.html', 
                           title='Add Record',
                           form=form,
                           events=app.config['EVENT_RECORDS']
                          )
