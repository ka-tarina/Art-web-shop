class ArtworkExceptionCode(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ArtworkNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
