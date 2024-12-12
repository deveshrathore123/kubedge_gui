from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route for static website technologies
@app.route('/static')
def static_page():
    return render_template('static/static.html')

# Static sub-pages
@app.route('/static/html')
def static_html():
    return render_template('static/html.html')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
