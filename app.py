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
    docker_image = request.form.get('docker_image', '')  # Default to empty if not provided
    container_port = request.form.get('container_port', '80')  # Default to 80 if not provided
    access_port = request.form.get('access_port', '8080')  # Default to 8080 if not provided

    # Pass these details to the shell script
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
        result = subprocess.run(shell_command, capture_output=True, text=True, check=True)

        # If the script executes successfully, capture the output
        script_output = result.stdout
        error_output = result.stderr

        # Render the output to the 'submitted.html' page
        return render_template('submitted.html', 
                               process_name=process_name,
                               github_url=github_url,
                               local_directory=local_directory,
                               docker_image=docker_image,
                               container_port=container_port,
                               access_port=access_port,
                               script_output=script_output,
                               error_output=error_output)
    
    except subprocess.CalledProcessError as e:
        # If there's an error in running the script, display it
        return f"An error occurred while executing the shell script: {e.stderr}"

# Route for dynamic website technologies
@app.route('/dynamic')
def dynamic_page():
    return render_template('dynamic/dynamic.html')

# Other routes (dynamic, database, etc.) as needed...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
