from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('html.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    process_name = request.form['process_name']
    github_url = request.form.get('github_url', '')
    local_directory = request.form['local_directory']
    docker_image = request.form.get('docker_image', '')
    container_port = request.form.get('container_port', '80')
    access_port = request.form.get('access_port', '8080')

    # Running the script (you can call your bash script here)
    # Assuming you have a bash script that runs the docker deploy logic
    script_output = subprocess.run(
        ['bash', './deploy_script.sh', process_name, github_url, local_directory, docker_image, container_port, access_port],
        capture_output=True, text=True
    )

    # Passing all the collected data and the script output to the 'submitted.html'
    return render_template('submitted.html', 
                           process_name=process_name, 
                           github_url=github_url,
                           local_directory=local_directory,
                           docker_image=docker_image,
                           container_port=container_port,
                           access_port=access_port,
                           script_output=script_output.stdout)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
