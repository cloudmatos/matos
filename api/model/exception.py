class ExceptionModel:
    def __init__(self, exception):
        self.message = exception['message']
        self.status = exception['status']
