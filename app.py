from flask import Flask, render_template, request, redirect, flash, url_for
import sqlite3
from datetime import datetime
from datetime import datetime, timezone


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for flashing messages

# Database initialization
DATABASE = 'database.db'
per_page = 10  # Number of logs per page

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ats_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                date_ts INTEGER,
                start TEXT,
                start_ts INTEGER,
                finish TEXT,
                finish_ts INTEGER,
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

def get_logs_n_pagination_data():
    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * per_page

    # Fetch data from the database with pagination
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, date, date_ts, start, start_ts, finish, finish_ts, initial, rating, remarks, ojti, examiner, trainee, op
            FROM ats_log ORDER BY id DESC 
            LIMIT ? OFFSET ?
        ''', (per_page, offset))
        logs = cursor.fetchall()

        # Get total count for pagination
        cursor.execute('SELECT COUNT(*) FROM ats_log')
        total_logs = cursor.fetchone()[0]

    # Calculate total pages
    total_pages = (total_logs + per_page - 1) // per_page
    return logs, page, total_pages

@app.route('/', methods=['GET'])
def index():
        return redirect('/new_ats_log_solo')


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

        date_sp = date.split('-')
        year = int(date_sp[0])
        month = int(date_sp[1])
        day = int(date_sp[2])

        start_sp = start.split(':')
        start_hour = int(start_sp[0])
        start_minute = int(start_sp[1])

        finish_sp = finish.split(':')
        finish_hour = int(finish_sp[0])
        finish_minute = int(finish_sp[1])

        # convert to unix tmiestamp
        date_ts = int(datetime(year, month, day, 0, 0, 0, 0, timezone.utc).timestamp())
        start_ts = int(datetime(year, month, day, start_hour, start_minute, 0, 0, timezone.utc).timestamp())
        finish_ts = int(datetime(year, month, day, finish_hour, finish_minute, 0, 0, timezone.utc).timestamp())


        # Validation
        # if not all([date, start, finish, initials, rating, remarks, ojti, examiner, trainee, op]):
        #     flash('All fields are required!', 'error')
        #     return redirect('/new_ats_log_solo')

        # Save to database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO ats_log (date, date_ts, start, start_ts, finish, finish_ts, initial, rating, remarks, ojti, examiner, trainee, op)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (date, date_ts, start, start_ts, finish, finish_ts, initials, rating, remarks, ojti, examiner, trainee, op))
            conn.commit()

        flash('Log saved successfully!', 'success')
        return redirect('/new_ats_log_solo')

    # Default data for date and UTC time
    current_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    current_utc_time = datetime.now(timezone.utc).strftime('%H:%M')  # Ensure 24-hour format
    options = ['Solo', 'OJT', 'Assessment']
    ratings = ['ADC','APP','APS','ATCA']
    initials = ['MO', 'AI', 'MS', 'AD', 'AL', 'AN', 'AS', 'AV', 'HA', 'HI', 'KR', 'MY', 'NA', 'AM', 'AR', 'MZ', 'MM', 'KS', 'SE', 'BI', 'SK', 'SH', 'BR', 'AB', 'LB', 'ME', 'MR', 'AO', 'MA']

    logs, page, total_pages = get_logs_n_pagination_data()

    return render_template('new_ats_log_solo.html', date=current_date, time=current_utc_time, ratings=ratings, initials=initials, options=options, logs=logs, page=page, total_pages=total_pages)

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

        
        date_sp = date.split('-')
        year = int(date_sp[0])
        month = int(date_sp[1])
        day = int(date_sp[2])

        start_sp = start.split(':')
        start_hour = int(start_sp[0])
        start_minute = int(start_sp[1])

        finish_sp = finish.split(':')
        finish_hour = int(finish_sp[0])
        finish_minute = int(finish_sp[1])

        # convert to unix tmiestamp
        date_ts = int(datetime(year, month, day, 0, 0, 0, 0, timezone.utc).timestamp())
        start_ts = int(datetime(year, month, day, start_hour, start_minute, 0, 0, timezone.utc).timestamp())
        finish_ts = int(datetime(year, month, day, finish_hour, finish_minute, 0, 0, timezone.utc).timestamp())


        # Validation
        # if not all([date, start, finish, initials, rating, remarks, ojti, examiner, trainee, op]):
        #     flash('All fields are required!', 'error')
        #     return redirect('/new_ats_log_ojt')

        # Save to database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO ats_log (date, date_ts, start, start_ts, finish, finish_ts, initial, rating, remarks, ojti, examiner, trainee, op)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (date, date_ts, start, start_ts, finish, finish_ts, initials, rating, remarks, ojti, examiner, trainee, op))
            conn.commit()

        flash('Log saved successfully!', 'success')
        return redirect('/new_ats_log_ojt')

    # Default data for date and UTC time
    current_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    current_utc_time = datetime.now(timezone.utc).strftime('%H:%M')  # Ensure 24-hour format
    options = ['OJT', 'Assessment', 'Solo']
    ratings = ['ADC','APP','APS','ATCA']
    initials = ['MO', 'AI', 'MS', 'AD', 'AL', 'AN', 'AS', 'AV', 'HA', 'HI', 'KR', 'MY', 'NA', 'AM', 'AR', 'MZ', 'MM', 'KS', 'SE', 'BI', 'SK', 'SH', 'BR', 'AB', 'LB', 'ME', 'MR', 'AO', 'MA']
    
    logs, page, total_pages = get_logs_n_pagination_data()
    return render_template('new_ats_log_ojt.html', date=current_date, time=current_utc_time, ratings=ratings, initials=initials, options=options, logs=logs, page=page, total_pages=total_pages)


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

        date_sp = date.split('-')
        year = int(date_sp[0])
        month = int(date_sp[1])
        day = int(date_sp[2])

        start_sp = start.split(':')
        start_hour = int(start_sp[0])
        start_minute = int(start_sp[1])

        finish_sp = finish.split(':')
        finish_hour = int(finish_sp[0])
        finish_minute = int(finish_sp[1])

        # convert to unix tmiestamp
        date_ts = int(datetime(year, month, day, 0, 0, 0, 0, timezone.utc).timestamp())
        start_ts = int(datetime(year, month, day, start_hour, start_minute, 0, 0, timezone.utc).timestamp())
        finish_ts = int(datetime(year, month, day, finish_hour, finish_minute, 0, 0, timezone.utc).timestamp())

        # Validation
        # if not all([date, start, finish, initials, rating, remarks, ojti, examiner, trainee, op]):
        #     flash('All fields are required!', 'error')
        #     return redirect('/new_ats_log_ojt')

        # Save to database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO ats_log (date, date_ts, start, start_ts, finish, finish_ts, initial, rating, remarks, ojti, examiner, trainee, op)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (date, date_ts, start, start_ts, finish, finish_ts, initials, rating, remarks, ojti, examiner, trainee, op))
            conn.commit()

        flash('Log saved successfully!', 'success')
        return redirect('/new_ats_log_assessment')

    # Default data for date and UTC time
    current_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    current_utc_time = datetime.now(timezone.utc).strftime('%H:%M')  # Ensure 24-hour format
    options = ['Assessment', 'Solo', 'OJT']
    ratings = ['ADC','APP','APS','ATCA']
    initials = ['MO', 'AI', 'MS', 'AD', 'AL', 'AN', 'AS', 'AV', 'HA', 'HI', 'KR', 'MY', 'NA', 'AM', 'AR', 'MZ', 'MM', 'KS', 'SE', 'BI', 'SK', 'SH', 'BR', 'AB', 'LB', 'ME', 'MR', 'AO', 'MA']
    
    logs, page, total_pages = get_logs_n_pagination_data()
    return render_template('new_ats_log_assessment.html', date=current_date, time=current_utc_time, ratings=ratings, initials=initials, options=options, logs=logs, page=page, total_pages=total_pages)

@app.route('/ats_logs', methods=['GET'])
def ats_logs():
    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * per_page

    # Fetch data from the database with pagination
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, date, start, finish, initial, rating, remarks, ojti, examiner, trainee, op
            FROM ats_log ORDER BY id DESC 
            LIMIT ? OFFSET ?
        ''', (per_page, offset))
        logs = cursor.fetchall()

        # Get total count for pagination
        cursor.execute('SELECT COUNT(*) FROM ats_log')
        total_logs = cursor.fetchone()[0]

    # Calculate total pages
    total_pages = (total_logs + per_page - 1) // per_page

    return render_template('ats_logs.html', logs=logs, page=page, total_pages=total_pages)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
