from flask import Flask, render_template, request, redirect, flash, url_for
import sqlite3
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for flashing messages

# Database initialization
DATABASE = 'database.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ats_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                start TEXT,
                finish TEXT,
                initial TEXT,
                rating TEXT,
                remarks TEXT,
                ojti TEXT,
                examiner TEXT,
                trainee TEXT,
                op TEXT
            )
        ''')
        conn.commit()
from datetime import datetime, timezone

@app.route('/new_ats_log_solo', methods=['GET', 'POST'])
def new_ats_log_solo():
    if request.method == 'POST':
        date = request.form.get('date')
        start = request.form.get('start')
        finish = request.form.get('finish')
        initials = request.form.get('initials')
        rating = request.form.get('rating')
        remarks = request.form.get('remarks')
        ojti = 'na'
        examiner = 'na'
        trainee = 'na'
        op = 'Solo'

        # Validation
        if not all([date, start, finish, initials, rating, remarks, ojti, examiner, trainee, op]):
            flash('All fields are required!', 'error')
            return redirect('/new_ats_log_solo')

        # Save to database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO ats_log (date, start, finish, initial, rating, remarks, ojti, examiner, trainee, op)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (date, start, finish, initials, rating, remarks, ojti, examiner, trainee, op))
            conn.commit()

        flash('Log saved successfully!', 'success')
        return redirect('/new_ats_log_solo')

    # Default data for date and UTC time
    current_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    current_utc_time = datetime.now(timezone.utc).strftime('%H:%M')  # Ensure 24-hour format
    options = ['Solo', 'OJT', 'Assessment']
    ratings = ['ADC','APP','APS','ATCA']
    initials = ['MO', 'AI', 'MS', 'AD', 'AL', 'AN', 'AS', 'AV', 'HA', 'HI', 'KR', 'MY', 'NA', 'AM', 'AR', 'MZ', 'MM', 'KS', 'SE', 'BI', 'SK', 'SH', 'BR', 'AB', 'LB', 'ME', 'MR', 'AO', 'MA']
    return render_template('new_ats_log_solo.html', date=current_date, time=current_utc_time, ratings=ratings, initials=initials, options=options)

@app.route('/new_ats_log_ojt', methods=['GET', 'POST'])
def new_ats_log_ojt():
    if request.method == 'POST':
        date = request.form.get('date')
        start = request.form.get('start')
        finish = request.form.get('finish')
        initials = 'na'
        rating = request.form.get('rating')
        remarks = request.form.get('remarks')
        ojti = request.form.get('ojti')
        examiner = 'na'
        trainee = request.form.get('trainee')
        op = 'OJT'

        # Validation
        if not all([date, start, finish, initials, rating, remarks, ojti, examiner, trainee, op]):
            flash('All fields are required!', 'error')
            return redirect('/new_ats_log_ojt')

        # Save to database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO ats_log (date, start, finish, initial, rating, remarks, ojti, examiner, trainee, op)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (date, start, finish, initials, rating, remarks, ojti, examiner, trainee, op))
            conn.commit()

        flash('Log saved successfully!', 'success')
        return redirect('/new_ats_log_ojt')

    # Default data for date and UTC time
    current_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    current_utc_time = datetime.now(timezone.utc).strftime('%H:%M')  # Ensure 24-hour format
    options = ['OJT', 'Assessment', 'Solo']
    ratings = ['ADC','APP','APS','ATCA']
    initials = ['MO', 'AI', 'MS', 'AD', 'AL', 'AN', 'AS', 'AV', 'HA', 'HI', 'KR', 'MY', 'NA', 'AM', 'AR', 'MZ', 'MM', 'KS', 'SE', 'BI', 'SK', 'SH', 'BR', 'AB', 'LB', 'ME', 'MR', 'AO', 'MA']
    return render_template('new_ats_log_ojt.html', date=current_date, time=current_utc_time, ratings=ratings, initials=initials, options=options)


@app.route('/new_ats_log_assessment', methods=['GET', 'POST'])
def new_ats_log_assessment():
    if request.method == 'POST':
        date = request.form.get('date')
        start = request.form.get('start')
        finish = request.form.get('finish')
        initials = 'na'
        rating = request.form.get('rating')
        remarks = request.form.get('remarks')
        ojti = request.form.get('ojti')
        examiner = request.form.get('examiner')
        trainee = request.form.get('trainee')
        op = 'Assessment'

        # Validation
        if not all([date, start, finish, initials, rating, remarks, ojti, examiner, trainee, op]):
            flash('All fields are required!', 'error')
            return redirect('/new_ats_log_ojt')

        # Save to database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO ats_log (date, start, finish, initial, rating, remarks, ojti, examiner, trainee, op)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (date, start, finish, initials, rating, remarks, ojti, examiner, trainee, op))
            conn.commit()

        flash('Log saved successfully!', 'success')
        return redirect('/new_ats_log_assessment')

    # Default data for date and UTC time
    current_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    current_utc_time = datetime.now(timezone.utc).strftime('%H:%M')  # Ensure 24-hour format
    options = ['Assessment', 'Solo', 'OJT']
    ratings = ['ADC','APP','APS','ATCA']
    initials = ['MO', 'AI', 'MS', 'AD', 'AL', 'AN', 'AS', 'AV', 'HA', 'HI', 'KR', 'MY', 'NA', 'AM', 'AR', 'MZ', 'MM', 'KS', 'SE', 'BI', 'SK', 'SH', 'BR', 'AB', 'LB', 'ME', 'MR', 'AO', 'MA']
    return render_template('new_ats_log_assessment.html', date=current_date, time=current_utc_time, ratings=ratings, initials=initials, options=options)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
