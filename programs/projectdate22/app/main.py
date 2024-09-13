from flask import Flask,render_template,request,Blueprint,url_for


main= Blueprint('main',__name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')

