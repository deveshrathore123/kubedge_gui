from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    app_type = request.form['appType']
    process_name = request.form['processName']
    
    # Logic for handling the submission
    # For now, let's just display a confirmation message
    message = f"Process {process_name} of type {app_type} is being deployed!"
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9876)
