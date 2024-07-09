from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import Course, db

admin = Blueprint('admin', __name__)

@admin.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('You do not have permission to access this page.')
        return redirect(url_for('main.home'))

    courses = Course.query.all()
    return render_template('admin.html', courses=courses)

@admin.route('/admin/add_course', methods=['POST'])
@login_required
def add_course():
    if not current_user.is_admin:
        flash('You do not have permission to access this page.')
        return redirect(url_for('main.home'))

    title = request.form.get('title')
    description = request.form.get('description')
    url = request.form.get('url')

    new_course = Course(title=title, description=description, url=url)
    db.session.add(new_course)
    db.session.commit()

    return redirect(url_for('admin.admin_dashboard'))

@admin.route('/admin/delete_course/<int:id>')
@login_required
def delete_course(id):
    if not current_user.is_admin:
        flash('You do not have permission to access this page.')
        return redirect(url_for('main.home'))

    course = Course.query.get(id)
    db.session.delete(course)
    db.session.commit()

    return redirect(url_for('admin.admin_dashboard'))