def app(environ,start_response):
    pairs = environ['QUERY_STRING'].split('&')
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body = '\n'.join(pairs)
    start_response(status, headers)
    return [ body ]
