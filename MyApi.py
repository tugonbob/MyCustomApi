from flask import *
import json
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def demo():
    data = {'page': 'Demo', 'message': 'Successfully called api demo', 'timestamp': time.time()}
    json_dump = json.dumps(data)

    return json_dump


@app.route('/user/', methods=['GET'])
def user():
    user_query = str(request.args.get('user'))
    data = {'page': 'User Info', 'message': f'{user_query}', 'timestamp': time.time()}
    json_dump = json.dumps(data)

    return json_dump

if __name__ == '__main__':
     app.run(port=8888)