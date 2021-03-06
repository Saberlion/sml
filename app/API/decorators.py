import json
from functools import wraps

from flask import request, Response,current_app

def jsonp(func):
    """Wraps JSONified output for JSONP requests."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)
    return decorated_function


class ResponseFormat:
    def __init__(self, code=0, msg='success', data_list=[]):
        self.code = code
        self.msg = msg
        self.data_list = data_list

    def get_dict(self):
        res = {'code': self.code, 'msg': self.msg, 'data': self.data_list}
        return res

    def get_json(self):
        res_dict = self.get_dict()
        return json.dumps(res_dict)


def auth(key=0):
    def _decorate(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            print request.json, key

            authkey = request.json.get('authkey')
            if authkey:
                from app.API.models import Auth
                auth_t = Auth()
                auth_t.authkey = authkey
                if auth_t.IsExist() and not auth_t.IsTimeOut():
                    return func(*args, **kwargs)

            rsps_str = ResponseFormat(403, 'authkey invalid')
            return Response(json.dumps(rsps_str.get_dict()), 403)

        return _wrapper

    return _decorate
