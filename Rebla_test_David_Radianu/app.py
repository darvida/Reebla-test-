from flask import Flask, render_template, jsonify
import requests


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

"""
The following fucntion is called upon by the javascript function which is activated by the button click    
"""
@app.route('/_get_data/', methods=['POST'])
def _get_data():

    external_api_request=requests.get('https://complimentr.com/api')
    requested_text=external_api_request.json()['compliment']

    return jsonify({'data': render_template('response.html', r_text=requested_text)})


if __name__ == "__main__":
    app.run(debug=True)