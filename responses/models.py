from django.db import models
from request.models import ItemRequest
from account.models import User

# Create your models here.
class ItemResponse(models.Model):
    request = models.ForeignKey(ItemRequest, on_delete=models.CASCADE, related_name="responses")
    responder = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("request", "responder")

    def __str__(self):
        return f"{self.responder} -> {self.request}"