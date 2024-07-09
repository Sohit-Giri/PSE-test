from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required, current_user
from models import Course

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('auth.login'))

@main.route('/home')
@login_required
def home():
    return render_template('home.html')

@main.route('/courses')
@login_required
def courses():
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

@main.route('/about')
@login_required
def about():
    return render_template('about.html')

@main.route('/contact')
@login_required
def contact():
    return render_template('contact.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@main.route('/course_detail/<int:id>')
@login_required
def course_detail(id):
    course = Course.query.get(id)
    return render_template('course_detail.html', course=course)

@main.route('/quiz/<int:course_id>')
@login_required
def quiz(course_id):
    return render_template('quiz.html', course_id=course_id)