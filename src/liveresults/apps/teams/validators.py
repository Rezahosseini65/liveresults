import os

from django.core.exceptions import ValidationError


def validate_png(image):
    ext = os.path.splitext(image.name)[1]
    valid_extensions = ['.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Only PNG files are allowed.')
