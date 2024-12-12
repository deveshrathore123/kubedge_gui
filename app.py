from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/host-static')
def host_static():
    return "Static Web Hosting Page"

@app.route('/host-dynamic')
def host_dynamic():
    return "Dynamic Web Hosting Page"

@app.route('/create-database')
def create_database():
    return "Create Database Page"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9876)
