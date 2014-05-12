access-manager
==============

The AccessManager object is intended to control access to resources, in a transparent way.
In order to do so, the object is created accepting two callables check_function and fail_handler, and exposes an access_required decorator.
Every time a decorated function is called, check_function will be called with decorator's parameters, and is expected to return 2 values (bool and dict):

* When validation succeeds, (True, data) -> AccessManager will call decorated function, appending data's values to keyword arguments.
* When validation fails, (False, data) -> AccessManager will call fail_handler, with data dictionary as keyword arguments.

## How to use access-manager

Just download a copy of access_manager.py and import the AccessManager object.
Write the check_function and the fail_handler and instantiate a copy with both.
Now you can decorate all the needed functions with the access_required decorator.

```python
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
```
