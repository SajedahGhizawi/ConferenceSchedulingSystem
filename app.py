from flask import Flask, render_template, request, redirect, session
import sqlite3
import bcrypt
import templates

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('conference_scheduling.db')
    conn.row_factory = sqlite3.Row
    return conn

# Registration route
@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    # Hash the password before storing it in the database
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert the user into the database (replace 'your_database.db' with your actual database filename)
    conn = get_db_connection()
    conn.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()

    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        session['logged_in'] = True
        session['email'] = email
        return redirect('/schedule')
    else:
        return 'Invalid email or password', 401  # Unauthorized status code

# Logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('email', None)
    return redirect('/')

# Schedule route (example restricted route)
@app.route('/schedule')
def schedule():
    if 'logged_in' in session and session['logged_in']:
        # Render the conference schedule page
        return 'Conference Schedule Page'
    else:
        return redirect('/login')
