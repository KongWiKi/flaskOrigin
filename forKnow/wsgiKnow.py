"""
@time : 2019/9/25下午4:12
@Author: kongwiki
@File: wsgiKnow.py
@Email: kongwiki@163.com
"""
from wsgiref.simple_server import make_server


def hello(environ, start_response):
	status = '200 ok'
	response_headers = [('Content-type', 'text/html')]
	name = environ['PATH_INFO'][1:]
	start_response(status, response_headers)
	return [b'<h1>Hello, Web</h1>' ]


# class AppClass:
# 	def __init__(self, environ, start_response):
# 		self.environ = environ
# 		self.start_response = start_response
#
# 	def __iter__(self):
# 		status = '200'
# 		response_headers = [('Content-type', 'text/html')]
# 		self.start_response(status, response_headers)
# 		yield b'<h1>Hello Web!</h1>'

server = make_server('localhost', 5000, hello)
server.serve_forever()
