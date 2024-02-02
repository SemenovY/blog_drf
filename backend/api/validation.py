from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_whitespace(value):
    if value.isspace():
        raise ValidationError(_("This field cannot consist only of whitespace."))
