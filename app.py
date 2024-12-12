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
        # Collecting the data from the form
        process_name = request.form['process_name']
        github_url = request.form.get('github_url')  # Optional
        local_directory = request.form['local_directory']
        docker_image = request.form.get('docker_image')  # Optional
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
        return render_template('submitted.html', process_name=process_name, github_url=github_url, 
                               local_directory=local_directory, docker_image=docker_image,
                               container_port=container_port, access_port=access_port)

    return render_template('static/html.html')  # This renders the form page on GET request

# Route for submitted details (success page)
@app.route('/submitted')
def submitted():
    return render_template('submitted.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
