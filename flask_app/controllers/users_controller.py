from flask_app import app
from flask import render_template, session, redirect, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User

bcrypt = Bcrypt(app)

# Home route with login and registration, if user logged in, redirects to dash
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/home')
    return render_template('index.html')

@app.route('/register')
def register():
    if 'user_id' in session:
        return redirect('/home')
    return render_template('register_page.html')

# Process any registration attempts and redirects to dash on success
@app.route('/users/register', methods=['POST'])
def process_registration():
    if not User.validate(request.form):
        return redirect('/register')
    
    pass_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': pass_hash,
    }

    user_id = User.create(data)
    session['user_id'] = user_id
    return redirect('/home')

@app.route('/login')
def login():
    if 'user_id' in session:
        return redirect('/home')
    return render_template('login_page.html')

# Process any login attempts and redirects to dash on success
@app.route('/users/login', methods=['POST'])
def process_login():
    potential_user = User.get_by_email(request.form)
    if not potential_user:
        flash('Invalid credentials. Try again.', 'log')
        return redirect('/login')
    elif not bcrypt.check_password_hash(potential_user.password, request.form['password']):
        flash('Invalid credentials. Try again.', 'log')
        return redirect('/login')
    
    session['user_id'] = potential_user.id
    return redirect('/home')
    
# Process logout
@app.route('/users/logout')
def logout():
    del session['user_id']
    return redirect('/')

# Home Page
@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('home.html')

# Life Tracker Page
@app.route('/lifetrack')
def life_tracker():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('/lifetrack_page.html')