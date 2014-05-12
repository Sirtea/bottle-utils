from bottle import Bottle, abort
from access_manager import AccessManager


def get_logged_user():
    return 'sirtea'


def validate_access(users):
    user = get_logged_user()
    if user in users:
        return True, {'user': user}
    return False, {'message': 'ERROR: Access denied'}


def fail_handler(message):
    abort(401, message)

app = Bottle()
am = AccessManager(validate_access, fail_handler)


@app.get('/admin')
@am.access_required(users=['admin', 'sirtea'])
def index(user):
    return 'Hello %s' % user
