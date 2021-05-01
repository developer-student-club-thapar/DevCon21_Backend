import uuid

from django.core.validators import RegexValidator
from django.db import models

MOBILE_REGEX = "^(\+\d{1,3}[- ]?)?\d{10}$"  # noqa
EVENT_CHOICES = (
    ("Webinar", "Webinar"),
    ("Designique", "Designique"),
    ("Both", "Both"),
)


class Participant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
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
    event = models.CharField(
        max_length=15, choices=EVENT_CHOICES, default="Webinar"
    )

    def __str__(self):
        return f"{self.name}"
