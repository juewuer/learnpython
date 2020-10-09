import subprocess
import itertools

use_ports = [8801, 8802]
use_http = ['http1.0', 'http1.1', 'http2']
def aaa():
	obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	obj.stdin.write(b'print( 1 ) \n')
	obj.stdin.write(b'print( 2 ) \n')
	obj.stdin.close()
	cmd_out = obj.stdout.read()
	obj.stdout.close()
	cmd_error = obj.stderr.read()
	obj.stderr.close()
	print (cmd_out)
	print (cmd_error)

use_ports = [8801]
use_http = ['http1.1', 'http2']
for (port, protocol) in itertools.product(use_ports,use_http):
	url =f'https://eatting.art:{port}/aaaa/bbb.txt'
	print(url)
	obj = subprocess.Popen(["curl", url, f'--{protocol}', '--cacert /root/keys/ca.crt', '-v', '-s'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	cmd_out = obj.stdout.read()
	obj.stdout.close()
	cmd_error = obj.stderr.read()
	obj.stderr.close()
	print (cmd_out)
	print (cmd_error)