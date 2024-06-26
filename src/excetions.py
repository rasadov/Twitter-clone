from fastapi import HTTPException

class Exception403(HTTPException):
    def __init__(self):
        self.status_code = 403
        self.detail = "Invalid data format"

class Exception404(HTTPException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Not found"
