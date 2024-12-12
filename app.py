from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for static website technologies
@app.route('/static')
def static_page():
    return render_template('static/static.html')

# Route for dynamic website technologies
@app.route('/dynamic')
def dynamic_page():
    return render_template('dynamic/dynamic.html')

# Route for database technologies
@app.route('/database')
def database_page():
    return render_template('database/database.html')

# Run the app on all available network interfaces
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
