from flask import Blueprint, render_template, request, redirect, url_for, session, current_app
from bson.objectid import ObjectId
from .models import student_collection
from flask_bcrypt import Bcrypt

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add', methods=('GET', 'POST'))
def add():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        age = request.form['age']
        student_collection.insert_one({'Student_id': student_id, 'name': name, 'age': age})
        return redirect(url_for('main.index'))

    return render_template('add.html')

@main.route('/edit', methods=['GET', 'POST'])
def edit():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        age = request.form['age']
        student_collection.insert_one({'Student_id': student_id, 'name': name, 'age': age})
        return redirect(url_for('main.index'))

    return render_template('add.html')

@main.route('/update/<student_id>', methods=['GET', 'POST'])
def update(student_id):  # Corrected function name
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    student = student_collection.find_one({'_id': ObjectId(student_id)})

    if request.method == 'POST':
        new_student_id = request.form['student_id']
        name = request.form['name']
        age = request.form['age']
        student_collection.update_one({'_id': ObjectId(student_id)}, {
            '$set': {'Student_id': new_student_id, 'name': name, 'age': age}})
        return redirect(url_for('main.index'))

    return render_template('edit.html', student=student)

@main.route('/delete/<student_id>')
def delete_student(student_id):
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    student_collection.delete_one({'_id': ObjectId(student_id)})
    return redirect(url_for('main.index'))
