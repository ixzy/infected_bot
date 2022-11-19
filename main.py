from flask import Flask, request, send_file
import os

app = Flask('app')


@app.route('/')
def hello_world():
  return 'Hello, World!'


@app.route('/l7')
def lol():
  uri = request.args['target']
  time = request.args['time']
  os.system(f'node net.js {uri} {time}')
  return 'Target:' + uri + '<br>Time:' + time


  
app.run(host='0.0.0.0', port=8080)
