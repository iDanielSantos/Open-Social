from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .models import get_user_by_username, add_user_to_db, check_password
from .utils.decorators import login_required, anonymous_required

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@auth_bp.route('/signin', methods=['GET', 'POST'])
@anonymous_required
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = get_user_by_username(username)

        if user:
            username, password_hash = user
            if check_password(password_hash, password):
                session['username'] = username
                return redirect(url_for('main.home'))

        flash('Usuário ou Senha incorretos', 'danger')

    return render_template('auth/signin.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
@anonymous_required
def signup():
    if request.method == 'POST':
        username = request.form['username']
        display_name = request.form['display_name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if get_user_by_username(username):
            flash('Alguém já usa esse username.', 'danger')
            return redirect(url_for('auth.signup'))

        if password != confirm_password:
            flash('As senhas não coincidem.', 'danger')
            return redirect(url_for('auth.signup'))

        add_user_to_db(username, display_name, password)

        session['username'] = username
        return redirect(url_for('main.home'))

    return render_template('auth/signup.html')

@auth_bp.route('/logout')
@login_required
def logout():
    session.clear()
    flash('Logout Bem-Sucedido.', 'info')
    return redirect(url_for('main.home'))