from inspect import getargspec
from json import dumps, load
from bottle import request, response


class JsonPlugin(object):

    def __init__(self, keyword):
        self.keyword = keyword

    def apply(self, callback, context):
        def wrapper(*args, **kwargs):
            _args = getargspec(callback)[0]
            if self.keyword in _args:
                try:
                    kwargs[self.keyword] = load(request.body)
                except:
                    kwargs[self.keyword] = None
            body, status = callback(*args, **kwargs)
            response.content_type = 'application/json'
            response.status = status
            if body is not None:
                return dumps(body, separators=(',', ':'))
            return ''
        return wrapper
