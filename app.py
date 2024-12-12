from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route for static website technologies
@app.route('/static')
def static_page():
    return render_template('static/static.html')

# Static sub-pages
@app.route('/static/html', methods=['GET', 'POST'])
def static_html():
    if request.method == 'POST':
        process_name = request.form['process_name']
        github_url = request.form.get('github_url')
        local_directory = request.form['local_directory']
        docker_image = request.form.get('docker_image')
        container_port = request.form.get('container_port', 80)  # Default to 80 if not provided
        access_port = request.form.get('access_port', 8080)  # Default to 8080 if not provided

        # Process the received data (store in database, log, etc.)
        print(f"Process Name: {process_name}")
        print(f"GitHub URL: {github_url}")
        print(f"Local Directory: {local_directory}")
        print(f"Docker Image: {docker_image}")
        print(f"Container Port: {container_port}")
        print(f"Access Port: {access_port}")

        # Redirect to a thank you page or confirmation page
        return "Details submitted successfully!"

    return render_template('static/html.html')  # This renders the form page on GET request

@app.route('/static/html-css')
def static_html_css():
    return render_template('static/html_css.html')

@app.route('/static/html-css-js')
def static_html_css_js():
    return render_template('static/html_css_js.html')

# Route for dynamic website technologies
@app.route('/dynamic')
def dynamic_page():
    return render_template('dynamic/dynamic.html')

# Dynamic sub-pages
@app.route('/dynamic/frontend')
def dynamic_frontend():
    return render_template('dynamic/frontend.html')

@app.route('/dynamic/backend')
def dynamic_backend():
    return render_template('dynamic/backend.html')

@app.route('/dynamic/additional-technologies')
def dynamic_additional_technologies():
    return render_template('dynamic/additional_technologies.html')

# Route for database technologies
@app.route('/database')
def database_page():
    return render_template('database/database.html')

# Database sub-pages
@app.route('/database/relational')
def relational_databases():
    return render_template('database/relational.html')

@app.route('/database/nosql')
def nosql_databases():
    return render_template('database/nosql.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
