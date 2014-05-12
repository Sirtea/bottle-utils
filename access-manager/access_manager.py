class AccessManager(object):

    def __init__(self, check_function, fail_handler):
        self.check_function = check_function
        self.fail_handler = fail_handler

    def access_required(self, *dec_args, **dec_kwargs):
        def wrapper1(target):
            def wrapper2(*args, **kwargs):
                ok, data = self.check_function(*dec_args, **dec_kwargs)
                if ok:
                    kwargs.update(data)
                    return target(*args, **kwargs)
                return self.fail_handler(**data)
            return wrapper2
        return wrapper1
