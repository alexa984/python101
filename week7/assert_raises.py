class unexpected_type_exception(Exception):
    def __init__(self):
        super().__init__('Unexpected type of error occured!')

class no_exception_occured(Exception):
    def __init__(self):
        super().__init__("The exception expected didn't happen!!")

class unexpected_message(Exception):
    def __init__(self):
        super().__init__("Unexpected message")

class assertRaises:
    def __init__(self, exception, msg = None):
        self.exception = exception
        self.msg = msg

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if type is not None:
            if type!=self.exception:
                raise unexpected_type_exception
            else:
                # if str(type)!=self.msg:
                #     raise
                return self
        else:
            raise no_exception_occured




with assertRaises(ZeroDivisionError):  # asserts SomeException is raised
    x = 5/1
    print(x)


