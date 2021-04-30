import uuid

from django.core.validators import RegexValidator
from django.db import models

MOBILE_REGEX = "^(\+\d{1,3}[- ]?)?\d{10}$"  # noqa


class Participant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    email = models.EmailField()
    referralCode = models.CharField(max_length=100, blank=True, null=True)
    yos_designation = models.CharField(max_length=100)
    mobile = models.CharField(
        max_length=16,
        validators=[
            RegexValidator(
                regex=MOBILE_REGEX,
                message="Enter a valid mobile number",
                code="invalid_mobile",
            )
        ],
    )

    def __str__(self):
        return f"{self.firstName} {self.lastName}"