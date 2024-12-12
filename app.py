from flask import Flask, render_template, request, redirect, url_for
import os
import subprocess

app = Flask(__name__)

# Function to check if Docker and Docker Compose are installed
def check_docker():
    try:
        subprocess.check_call(["docker", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.check_call(["docker-compose", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return False
    return True

# Route for the home page (Dashboard)
@app.route('/')
def index():
    if not check_docker():
        return render_template('index.html', error="Docker and Docker Compose are required but not installed.")
    return render_template('index.html')

# Route to handle static website deployment
@app.route('/deploy_static', methods=['GET', 'POST'])
def deploy_static():
    if request.method == 'POST':
        static_choice = request.form['static_choice']
        process_name = request.form['process_name'].lower()
        html_path = request.form['html_path']
        image_name = request.form['image_name']
        container_port = request.form['container_port']
        access_port = request.form['access_port']

        # Validate the input fields
        if not os.path.isfile(f"{html_path}/index.html"):
            return render_template('deploy_static.html', error="index.html not found in the specified directory.")
        
        # Validate Docker and Compose
        if not check_docker():
            return render_template('deploy_static.html', error="Docker and Docker Compose are required but not installed.")
        
        # Create Dockerfile and docker-compose.yml
        dockerfile_content = """FROM nginx:alpine
COPY . /usr/share/nginx/html
"""
        docker_compose_content = f"""version: '3'
services:
  web:
    build:
      context: .
    ports:
      - "{access_port}:{container_port}"
    restart: always
"""

        # Write Dockerfile and docker-compose.yml
        with open(f"{html_path}/Dockerfile", "w") as f:
            f.write(dockerfile_content)
        
        with open(f"{html_path}/docker-compose.yml", "w") as f:
            f.write(docker_compose_content)
        
        # Change directory to html_path and run Docker Compose
        os.chdir(html_path)
        subprocess.run(['docker-compose', 'up', '--build', '-d'])

        return render_template('deploy_static.html', success=f"Static website deployed successfully! Access it at http://localhost:{access_port}")

    return render_template('deploy_static.html')


# Route for dynamic web hosting (placeholder)
@app.route('/deploy_dynamic')
def deploy_dynamic():
    return render_template('deploy_dynamic.html')

if __name__ == '__main__':
    app.run(debug=True, port=9876)
