class OrderExceptionCode(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class OrderNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class InvalidOrderStatusError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
