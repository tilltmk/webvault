from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Website
from app.utils import download_website, generate_pdf

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please login.')
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/dashboard')
@login_required
def dashboard():
    websites = current_user.websites
    return render_template('dashboard.html', websites=websites)

@main.route('/add_website', methods=['POST'])
@login_required
def add_website():
    url = request.form['url']
    website = Website(url=url, domain=extract_domain(url), user=current_user)
    db.session.add(website)
    db.session.commit()
    download_website(website)
    generate_pdf(website)
    flash('Website added successfully')
    return redirect(url_for('main.dashboard'))

@main.route('/website/<int:website_id>')
@login_required
def view_website(website_id):
    website = Website.query.get_or_404(website_id)
    if website.user != current_user:
        abort(403)
    return render_template('website_view.html', website=website)