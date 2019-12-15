from wsgiref.simple_server import make_server

def web_app(enviroment, response):
    status = '200 OK'
    headers = [('Conetent-type', "text/html; charset=utf-8")]

    response(status, headers)

    return [b'<h1>Hello World i just created my first WSGi</h1>']

with make_server('', 8000, web_app) as server:

    print("Serving on port 8000....\n Visit http://127.0.0.1:8000\n To kill the server 'contro + C")

    server.serve_forever()