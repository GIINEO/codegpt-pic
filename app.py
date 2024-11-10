from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    response = requests.get('https://httpbin.org/get')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
