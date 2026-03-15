from django.db import models
from account.models import User

from django.db import models
from account.models import User

class UserReport(models.Model):
    ACTIVITY_CHOICES = [
        ("spam", "Spam"),
        ("harassment", "Harassment"),
        ("scam", "Scammer"),
        
        ("inappropriate_content", "Inappropriate Content"),

        ("other", "Other"),
    ]

    reported_user = models.ForeignKey(
        User,
        related_name="reports_received",
        on_delete=models.CASCADE
    )

    reported_by = models.ForeignKey(
        User,
        related_name="reports_made",
        on_delete=models.CASCADE
    )

    activity_type = models.CharField(
        max_length=50,
        choices=ACTIVITY_CHOICES,
        default="other"
    )

    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("reported_user", "reported_by", "activity_type")
    # Note prevent self report
    # if request.owner == request.user:
    # block response
