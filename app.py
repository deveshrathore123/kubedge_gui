from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route for static website technologies
@app.route('/static')
def static_page():
    return render_template('static/static.html')

# Static sub-pages
@app.route('/static/html', methods=['GET'])
def static_html():
    return render_template('static/html.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_details():
    # Capture form details
    process_name = request.form['process_name']
    github_url = request.form.get('github_url')
    local_directory = request.form['local_directory']
    docker_image = request.form.get('docker_image', '')
    container_port = request.form.get('container_port', '80')  # Default to 80 if not provided
    access_port = request.form.get('access_port', '8080')  # Default to 8080 if not provided

    # Pass these details to the shell script
    # Ensure you pass them in the proper order as per the shell script arguments
    try:
        # Construct the command to run the shell script
        shell_command = [
            '/bin/bash', 'deploy_static.sh',
            process_name,
            github_url or '',  # If GitHub URL is empty, pass an empty string
            local_directory,
            docker_image or '',  # If Docker image is empty, pass an empty string
            container_port,
            access_port
        ]

        # Execute the shell script
        subprocess.run(shell_command, check=True)

        # Redirect to a confirmation or success page
        return "Details submitted successfully! Your static web app is being deployed."

    except subprocess.CalledProcessError as e:
        return f"An error occurred while executing the shell script: {e}"

# Route for dynamic website technologies
@app.route('/dynamic')
def dynamic_page():
    return render_template('dynamic/dynamic.html')

# Other routes (dynamic, database, etc.) as needed...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
