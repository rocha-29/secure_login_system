from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime
from cryptography.fernet import Fernet
import json
import os
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cámbiala en producción

# Rutas de archivos
KEY_FILE = 'data/secret.key'
USERS_FILE = 'data/users.json'

# Cargar clave Fernet desde archivo
def load_key():
    with open(KEY_FILE, 'rb') as f:
        return f.read()

# Cargar usuarios (descifrado)
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}

    key = load_key()
    fernet = Fernet(key)

    try:
        with open(USERS_FILE, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())
    except Exception as e:
        print("❌ Error decrypting users file:", e)
        return {}

# Guardar usuarios (cifrado)
def save_users(users):
    key = load_key()
    fernet = Fernet(key)

    json_data = json.dumps(users).encode()
    encrypted_data = fernet.encrypt(json_data)

    with open(USERS_FILE, 'wb') as f:
        f.write(encrypted_data)

# Cargar usuarios en memoria al iniciar
users = load_users()

# Decorador personalizado para rutas protegidas
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('You must be logged in to view this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Mostrar año actual en todas las plantillas
@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']

        user_password = users.get(username)
        if user_password and check_password_hash(user_password, password):
            session['username'] = username
            flash(f'Welcome back, {username}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']

        if username in users:
            flash('Username already exists. Please choose another.', 'danger')
            return redirect(url_for('register'))

        # Validación avanzada de contraseña
        if len(password) < 8:
            flash('Password must be at least 8 characters long.', 'danger')
            return redirect(url_for('register'))
        if not re.search(r"[A-Z]", password):
            flash('Password must contain at least one uppercase letter.', 'danger')
            return redirect(url_for('register'))
        if not re.search(r"[a-z]", password):
            flash('Password must contain at least one lowercase letter.', 'danger')
            return redirect(url_for('register'))
        if not re.search(r"\d", password):
            flash('Password must contain at least one number.', 'danger')
            return redirect(url_for('register'))
        if not re.search(r"\W", password):
            flash('Password must contain at least one special character.', 'danger')
            return redirect(url_for('register'))

        # Guardar usuario
        hashed_password = generate_password_hash(password)
        users[username] = hashed_password
        save_users(users)
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=session['username'])

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
