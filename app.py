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
                initials TEXT,
                position TEXT,
                remarks TEXT
            )
        ''')
        conn.commit()
from datetime import datetime, timezone

@app.route('/new_ats_log', methods=['GET', 'POST'])
def new_ats_log():
    if request.method == 'POST':
        date = request.form.get('date')
        start = request.form.get('start')
        finish = request.form.get('finish')
        initials = request.form.get('initials')
        position = request.form.get('position')
        remarks = request.form.get('remarks')

        # Validation
        if not all([date, start, finish, initials, position, remarks]):
            flash('All fields are required!', 'error')
            return redirect('/new_ats_log')

        # Save to database
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO ats_log (date, start, finish, initials, position, remarks)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (date, start, finish, initials, position, remarks))
            conn.commit()

        flash('Log saved successfully!', 'success')
        return redirect('/new_ats_log')

    # Default data for date and UTC time
    current_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    current_utc_time = datetime.now(timezone.utc).strftime('%H:%M')  # Ensure 24-hour format
    positions = ['ADC','APP','APS','ATCA']
    initials = ['MO', 'AI', 'MS', 'AD', 'AL', 'AN', 'AS', 'AV', 'HA', 'HI', 'KR', 'MY', 'NA', 'AM', 'AR', 'MZ', 'MM', 'KS', 'SE', 'BI', 'SK', 'SH', 'BR', 'AB', 'LB', 'ME', 'MR', 'AO', 'MA']
    return render_template('new_ats_log.html', date=current_date, time=current_utc_time, positions=positions, initials=initials)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
