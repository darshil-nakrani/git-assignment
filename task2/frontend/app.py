from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

BACKEND_URL = 'http://127.0.0.1:9000'

@app.route('/')
def home():
    return "This is the frontend"

@app.route('/form')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    response = requests.post(BACKEND_URL + '/submit', json=form_data)

    if response.status_code == 200:
        result = response.json()
        if result.get('success'):
            return redirect(url_for('success'))
        else:
            return f'Error: {result.get('message')}'
    else:
        return "Something went wrong with backend"
    
@app.route('/success')
def success():
    return "Data submitted successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)