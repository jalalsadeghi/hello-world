import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = os.getenv('MESSAGE', 'Hello World!')
    return message



#test
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)