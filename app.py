from flask import Flask, render_template, request

app = Flask(__name__)

# Home route to render the form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission (will be updated later with deployment functionality)
@app.route('/deploy', methods=['POST'])
def deploy():
    if request.method == 'POST':
        # Retrieve form data
        static_choice = request.form['static_choice']
        process_name = request.form['process_name']
        html_path = request.form['html_path']
        container_port = request.form['container_port']
        access_port = request.form['access_port']
        
        # For now, we'll just print the data
        return f"Form submitted with: Static Choice: {static_choice}, Process Name: {process_name}, HTML Path: {html_path}, Container Port: {container_port}, Access Port: {access_port}"

# Start the Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876)
