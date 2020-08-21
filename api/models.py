from django.db import models
from datetime import datetime

# Create your models here.


class ResponseMessage:
    def __init__(self, message,  exception, content=None, status=None, created=None):
        self.message = message
        self.content = content
        self.created = created or datetime.now()
        self.exception = exception
        self.status = status