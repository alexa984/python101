class Unexpected_type_exception(Exception):
    def __init__(self):
        super().__init__('Unexpected type of error occured!')

class No_exception_occured(Exception):
    def __init__(self):
        super().__init__("The exception expected didn't happen!!")

class Unexpected_message(Exception):
    def __init__(self):
        super().__init__("Unexpected message")

class AssertRaises:
    def __init__(self, exception, msg = None):
        self.exception = exception
        self.msg = msg

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if type is not None:
            if type!=self.exception:
                raise Unexpected_type_exception
            else:
                return self
        else:
            raise No_exception_occured



