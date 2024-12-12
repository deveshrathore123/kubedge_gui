from flask import Flask, render_template

# Create the Flask application
app = Flask(__name__)

# Route for the main page
@app.route('/')
def home():
    return render_template('home.html')

# Placeholder route for hosting static web
@app.route('/host-static')
def host_static():
    return "Static Web Hosting Page"

# Placeholder route for hosting dynamic web
@app.route('/host-dynamic')
def host_dynamic():
    return "Dynamic Web Hosting Page"

# Placeholder route for creating a database
@app.route('/create-database')
def create_database():
    return "Create Database Page"

# Start the Flask app with debug mode and listen on all interfaces (0.0.0.0) at port 9876
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9876)
