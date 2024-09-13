from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello"
@app.route('/home')
def hello_wld():
    return render_template('home.html')

@app.route('/about')
def hello_wold():
    return render_template('about.html')

@pp.route('/projects')
def project():
    return render_template('projects.html')



if(__name__)== "__main__":
    app.run(debug=True)