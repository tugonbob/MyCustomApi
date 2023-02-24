from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def demo():
    if request.method == 'GET':
        query = str(request.args.get('query'))
        data = {'method': "GET", 'query': query}
        return json.dumps(data)
    else:
        query = request.form['query']
        data = {'method': 'POST', 'query': query}
        return json.dumps(data)


if __name__ == '__main__':
     app.run(port=8888)