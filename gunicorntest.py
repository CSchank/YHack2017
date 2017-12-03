def app(environ, start_response):
    """Simplest possible application object"""
    data = 'Goodbye world!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return [bytes(data, 'utf-8')]