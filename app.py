from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "abc Hello World!"

@app.route('/receive/text/<string:text>')
def send_back_text(text):
    return text

@app.route('/receive/json/', methods=["POST"])
def send_back_text_json():
    if request.method == "POST":
        json_dict = request.get_json()
        text = json_dict['text']
        data = {'text': text, 'textTwice': (text + ", " + text)}
        return jsonify(data)
    else:
        return 'not a post request'

# curl -d '{"text":"abc"}' -H "Content-Type: application/json" -X POST http://localhost:5000/receive/json/

# curl -d '{"lilypond":"abc","shortscore":""}' -H "Content-Type: application/json" -X POST http://localhost:5000/check/
@app.route('/check/', methods=["POST"])
def check():
    if request.method == "POST":
        json_dict = request.get_json()
        lilypond = json_dict['lilypond']
        shortscore = json_dict['shortscore']
        data = {'check': lilypond == 'abc'}
        return jsonify(data)
    else:
        return 'not a post request'


@app.route('/download/')
def download_file():
    return send_from_directory('.', 'shortscoreOutput.zip', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
