from django.core.exceptions import ValidationError


def validate_age(value):
    if not value.isdigit() or value < 0:
        raise ValidationError("Invalid age!!!")