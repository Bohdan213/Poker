from flask import Flask, jsonify, request
import get_method

app = Flask(__name__, static_url_path='/static/', static_folder='static')


@app.route('/probabilities', methods=['POST'])
def get_probabilities():
    return jsonify(get_method.process(request.json)), 200


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(port=80)
