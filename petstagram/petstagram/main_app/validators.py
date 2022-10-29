import re

from django.core.exceptions import ValidationError


def validate_name(value):
    if len(value) < 2:
        raise ValidationError("The name should have at least 2 chars!!!")
    elif not value.isalpha():
        raise ValidationError("The name should consist only of letters!!!")
    return value


def validate_email(value):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if not (re.fullmatch(regex, value)):
        raise ValidationError('Invalid email!!!')
    return value